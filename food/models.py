#food
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Food(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField( max_length=255, )
    nutrition = models.TextField()
    
    def get_absolute_url(self):
        return reverse('food: food', {'pk': self.pk })
    def __str__(self):
        return self.name 