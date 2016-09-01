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
    
    #Proximates
    water = models.DecimalField(max_digits=7, decimal_places=5)
    energy = models.DecimalField(max_digits=7, decimal_places=5)
    protein = models.DecimalField(max_digits=7, decimal_places=5)
    lipid = models.DecimalField(max_digits=7, decimal_places=5)
    carbohydrate = models.DecimalField(max_digits=7, decimal_places=5)
    fiber = models.DecimalField(max_digits=7, decimal_places=5)
    sugar = models.DecimalField(max_digits=7, decimal_places=5)
    #Minerals
    calcium = models.DecimalField(max_digits=7, decimal_places=5)
    iron = models.DecimalField(max_digits=7, decimal_places=5)
    magnesium = models.DecimalField(max_digits=7, decimal_places=5)
    phosphorus = models.DecimalField(max_digits=7, decimal_places=5)
    potassium = models.DecimalField(max_digits=7, decimal_places=5)
    sodium = models.DecimalField(max_digits=7, decimal_places=5)
    zinc = models.DecimalField(max_digits=7, decimal_places=5)
    #Vitamins
    ascorbic = models.DecimalField(max_digits=7, decimal_places=5)
    thiamin = models.DecimalField(max_digits=7, decimal_places=5)
    riboflavin = models.DecimalField(max_digits=7, decimal_places=5)
    niacin = models.DecimalField(max_digits=7, decimal_places=5)
    pyridoxine = models.DecimalField(max_digits=7, decimal_places=5)
    folate = models.DecimalField(max_digits=7, decimal_places=5)
    cobalamin = models.DecimalField(max_digits=7, decimal_places=5)
    retinol = models.DecimalField(max_digits=7, decimal_places=5)
    betacarotene = models.DecimalField(max_digits=7, decimal_places=5)
    tocopheryl = models.DecimalField(max_digits=7, decimal_places=5)
    ergocalciferol  = models.DecimalField(max_digits=7, decimal_places=5)
    cholecalciferol  = models.DecimalField(max_digits=7, decimal_places=5)
    phylloquinone = models.DecimalField(max_digits=7, decimal_places=5)
    #Lipids
    saturated = models.DecimalField(max_digits=7, decimal_places=5)
    monounsaturated = models.DecimalField(max_digits=7, decimal_places=5)
    polyunsaturated = models.DecimalField(max_digits=7, decimal_places=5)
    cholesterol = models.DecimalField(max_digits=7, decimal_places=5)
    #Other
    caffeine = models.DecimalField(max_digits=7, decimal_places=5)
    
    def get_absolute_url(self):
        return reverse('food: food', {'pk': self.pk })
    def __str__(self):
        return self.name 