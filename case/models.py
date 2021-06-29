from typing import Tuple
from django.contrib.admin.options import VERTICAL
from django.db import models
from django import forms

# Create your models here.

from django.db import models
from django.db.models.fields import CharField, TextField

CASE_TYPES = (
        ('ГР', 'Гражданское'),
        ('УГ', 'Уголовное')

)

SERVICE_TYPE = (
        ('К', 'Консультация'),
        ('У', 'Учасите')

)

class ClientCase(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    client_name = models.CharField(verbose_name='Имя клиента', max_length=100)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    case_type = models.CharField(verbose_name='Тип дела', max_length=300, choices = CASE_TYPES)
    paintiff = models.CharField(verbose_name='Истец', max_length=100)
    defendant = models.CharField(verbose_name='Ответчик', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=250)
    date = models.DateTimeField(verbose_name='Дата добавления')
    service_type = models.CharField(verbose_name="Тип услуг", max_length=300,choices = SERVICE_TYPE) 
    case_status = models.CharField(verbose_name='Статус дела', max_length=100, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'