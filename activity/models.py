#activity
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Activity(models.Model):
    exercise = models.CharField(max_length = 255)
    weight1 = models.IntegerField(default = 0)
    weight2 = models.IntegerField(default = 0)
    weight3 = models.IntegerField(default = 0)
    weight4 = models.IntegerField(default = 0)
   # weight1 = 130lbs, weight2 = 155lbs, weight3 = 180lbs and weight4 = 205lbs
   # calories burned are per hour 
    def __str__(self):
        return self.exercise 
   