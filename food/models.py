#food
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Food(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField( max_length=255, )
    image = models.CharField( max_length=255, )
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255, )
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    contents = models.TextField()
    
    # #Proximates
    # water = models.CharField(max_length = 255)
    # energy = models.CharField(max_length = 255)
    # protein = models.CharField(max_length = 255)
    # lipid = models.CharField(max_length = 255)
    # carbohydrate = models.CharField(max_length = 255)
    # fiber = models.CharField(max_length = 255)
    # sugar = models.CharField(max_length = 255)
    # #Minerals
    # calcium = models.CharField(max_length = 255)
    # iron = models.CharField(max_length = 255)
    # magnesium = models.CharField(max_length = 255)
    # phosphorus = models.CharField(max_length = 255)
    # potassium = models.CharField(max_length = 255)
    # sodium = models.CharField(max_length = 255)
    # zinc = models.CharField(max_length = 255)
    # #Vitamins
    # ascorbic = models.CharField(max_length = 255)
    # thiamin = models.CharField(max_length = 255)
    # riboflavin = models.CharField(max_length = 255)
    # niacin = models.CharField(max_length = 255)
    # pyridoxine = models.CharField(max_length = 255)
    # folate = models.CharField(max_length = 255)
    # cobalamin = models.CharField(max_length = 255)
    # retinol = models.CharField(max_length = 255)
    # betacarotene = models.CharField(max_length = 255)
    # tocopheryl = models.CharField(max_length = 255)
    # ergocalciferol  = models.CharField(max_length = 255)
    # cholecalciferol  = models.CharField(max_length = 255)
    # phylloquinone = models.CharField(max_length = 255)
    # #Lipids
    # saturated = models.CharField(max_length = 255)
    # monounsaturated = models.CharField(max_length = 255)
    # polyunsaturated = models.CharField(max_length = 255)
    # cholesterol = models.CharField(max_length = 255)
    # #Other
    # caffeine = models.CharField(max_length = 255)
    
    def get_absolute_url(self):
        return reverse('food: food', {'pk': self.pk })
    def __str__(self):
        return self.name 