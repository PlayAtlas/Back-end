from django.http.response import JsonResponse
from django.shortcuts import render

def user_detail(request):
    return JsonResponse({'user': 'User 1'})