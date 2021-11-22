from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotAllowed

all_chartsets = [
        {'id': 1, 'charts': 2, 'name': 'Test'},
        {'id': 2, 'charts': 5, 'name': 'Laba 5.1a'},
        {'id': 3, 'charts': 6, 'name': 'Laba 5.7'},
        {'id': 4, 'charts': 3, 'name': 'Laba 5.12'},
        {'id': 5, 'charts': 4, 'name': 'Laba 5.14'},
    ]

#Создание объекта
def create_chartset(request, chartset_id, chartset_name):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))

    return JsonResponse({'id': chartset_id, 'charts': 0, 'name': chartset_name})

#Список объектов
def list_chartsets(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(('GET',))
    return JsonResponse({'saved chartsets': all_chartsets})

#Детальная информация об объекте
def chartset_detail(request, chartset_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(('GET',))
    return JsonResponse(all_chartsets[chartset_id + 1])

#Функция, которая возвращает отрендеренный html (например, главная страница приложения)
def home(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(('GET',))
    return render(request, 'index.html')