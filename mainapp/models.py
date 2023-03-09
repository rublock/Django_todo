from django.db import models
from django.contrib.auth.models import User


class DataBase(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(max_length=9999, verbose_name='Description')
    image = models.ImageField(upload_to='static/img', verbose_name='Image')
    url = models.URLField(blank=True, verbose_name='Url')

    '''отображение записей в списке в админке'''
    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
