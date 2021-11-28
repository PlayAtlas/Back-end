from django.db import models

class Chartset(models.Model):
    #Первичный ключ не создаем
    name = models.CharField(max_length=32, verbose_name='Название проекта')


