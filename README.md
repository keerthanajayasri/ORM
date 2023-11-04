# Ex02 Django ORM Web Application
## Date: 4/11/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import player,playerAdmin
admin.site.register(player,playerAdmin)

models.py

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
```

## OUTPUT

![Alt text](<Screenshot (15).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
