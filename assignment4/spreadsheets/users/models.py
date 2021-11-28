from django.db import models
from django.db.models.fields import EmailField

from chartsets.models import Chartset
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Почта')
    userschartsets = models.ManyToManyField(Chartset, verbose_name='Проект')
