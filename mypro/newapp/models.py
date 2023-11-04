

from django.db import models
from django.contrib import admin
class player (models.Model):
    team=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    goals=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class playerAdmin(admin.ModelAdmin):
    list_display=('team','name','goals','age','email')

