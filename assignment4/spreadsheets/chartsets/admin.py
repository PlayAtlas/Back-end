# Register your models here.
from django.contrib import admin
from chartsets.models import Chartset

class ChartsetAdmin(admin.ModelAdmin):
    list_filter = ('userschartsets',)
    list_display = ('name', 'date_modified')

admin.site.register(Chartset, ChartsetAdmin)