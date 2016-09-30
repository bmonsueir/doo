#food
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Food(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField( max_length=255, )
    code = models.IntegerField(default = 0)
    group = models.IntegerField(default = 0)
    class Meta:
        ordering = ["name"]
   
    def __str__(self):
        return self.name 
   
        
class Method(models.Model):
    name = models.CharField(max_length = 255)
    abrev = models.CharField( max_length=255, )
    code = models.IntegerField(default = 0)
    unit = models.CharField( max_length=255, )
   
    def __str__(self):
        return self.name 
        
class Nutrition(models.Model):
    value = models.DecimalField(max_digits = 11, decimal_places = 4)
    food = models.IntegerField(default = 0)
    test = models.IntegerField(default = 0)
   
    def __str__(self):
        return self.food 