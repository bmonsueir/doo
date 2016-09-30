from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
from food.models import Food 
from activity.models import Activity


class Meal(models.Model):
    food = models.ForeignKey(Food, default=1)
    amount = models.DecimalField(max_digits = 11, decimal_places = 4)
    description = models.CharField( max_length=255, )
    client = models.ForeignKey(User, default=1)
    timeOf = models.DateTimeField('date created', default=datetime.now)
    class Meta:
        ordering = ["timeOf"]    
    def __str__(self):
        return self.food 
        
class Condition(models.Model):
    health = models.CharField( max_length=255,)
    weight = models.CharField( max_length=255, )
    client = models.ForeignKey(User, default=1)
    height = models.CharField(max_length=255, )
    timeOf = models.DateTimeField('date created', default=datetime.now)
    class Meta:
        ordering = ["timeOf"]
    
    def __str__(self):
        return self.name 
        
class Movement(models.Model):
    name = models.ForeignKey(Activity, default = 1)
    client = models.ForeignKey(User, default=1)
    description = models.CharField( max_length=255, )
    amount = models.IntegerField(default = 0)
    timeOf = models.DateTimeField('date created', default=datetime.now)
    
    class Meta:
        ordering = ["timeOf"]
        
    def __str__(self):
        return self.name 
        
