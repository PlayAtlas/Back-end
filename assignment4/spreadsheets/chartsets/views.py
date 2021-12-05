from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseNotFound
from chartsets.models import Chartset
from users.models import User
from chartsets.serializers import ChartsetSerializer
from rest_framework import viewsets
from rest_framework.response import Response
#Создание объекта---работает
@require_POST
def create_chartset(request):
    newchartset = Chartset.objects.create(name=request.POST.get('chartset_name'))
    usr = User.objects.first()
    print(usr)
    newchartset.userschartsets.add(usr)
    print(newchartset.userschartsets)
    #не нужен сейв
    return JsonResponse({'pk': newchartset.pk, 'name': request.POST.get('chartset_name')})

#Детальная информация об объекте---работает
@require_GET
def chartset_detail(request, chartset_id):
    try:
        mychartset = Chartset.objects.get(id=chartset_id)
    except Chartset.DoesNotExist:
        return HttpResponseNotFound('Chartset not found')
    return JsonResponse({'id': mychartset.id, 'name': mychartset.name, 'Последнее изменение': mychartset.date_modified})

#Редактирование объекта---работает
@require_POST
def edit_chartset(request, chartset_id):
    try:
        mychartset = Chartset.objects.get(id=chartset_id)
    except Chartset.DoesNotExist:
        return HttpResponseNotFound('Chartset not found')
    old_name = mychartset.name
    mychartset.name = request.POST.get('new_name')
    mychartset.save()
    return JsonResponse({'old name': old_name, 'new name': mychartset.name})

#Удаление объекта---работает
@require_POST
def delete_chartset(request, chartset_id):
    try:
        mychartset = Chartset.objects.get(id=chartset_id)
    except Chartset.DoesNotExist:
        return HttpResponseNotFound('Chartset not found')
    name = mychartset.name
    mychartset.delete()
    return JsonResponse({'deleted chartset': name})

#Список объектов---работает
@require_GET
def list_chartsets(request):
    allchartsets = Chartset.objects.all()
    resp =[]
    for obj in allchartsets:
        resp.append({'id': obj.id, 'name': obj.name})
    return JsonResponse({'all chartsets': resp})

#Функция, которая возвращает отрендеренный html (например, главная страница приложения)
@require_GET
def home(request):
    return render(request, 'index.html')
    
#проверка реляционной связи
#SELECT chartsets_chartset.name, users_user.username FROM chartsets_chartset INNER JOIN chartsets_chartset_userschartsets ON chartsets_chartset_userschartsets.chartset_id = chartsets_chartset.id INNER JOIN users_user ON chartsets_chartset_userschartsets.user_id = users_user.id;

class ChartsetViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Chartset.objects.all()
        serializer = ChartsetSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        queryset = Chartset.objects.all()
        chartset = get_object_or_404(queryset, pk=pk)
        serializer = ChartsetSerializer(chartset)
        return Response(serializer.data)