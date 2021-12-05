from django.http.response import JsonResponse
from django.shortcuts import render
from users.models import User

def user_detail(request):
    return JsonResponse({'user': 'User 1'})