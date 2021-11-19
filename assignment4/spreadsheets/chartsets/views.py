from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

def chartset_detail(request, chartset_id):
    return JsonResponse({'chartset': chartset_id})