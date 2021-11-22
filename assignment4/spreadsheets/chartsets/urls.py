from django.contrib import admin
from django.urls import path
from chartsets.views import chartset_detail, home, create_chartset, list_chartsets

urlpatterns = [
    path('chartset/<int:chartset_id>/', chartset_detail, name='chartset_detail'),
    path('create_chartset/<int:chartset_id>/<str:chartset_name>/', create_chartset, name='create_chartset'),
    path('list/', list_chartsets, name='list_chartsets'),
    path('home/', home, name='home'),
]