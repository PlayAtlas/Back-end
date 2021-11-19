from django.contrib import admin
from django.urls import path
from chartsets.views import chartset_detail

urlpatterns = [
    path('chartset/<int:chartset_id>/', chartset_detail, name='chartset_detail'),

]