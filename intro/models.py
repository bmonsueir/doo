#intro
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Tutorial(models.Model):
    name = models.CharField(max_length = 255)
    link = models.URLField()
    description = models.CharField( max_length=255, )
   
    def __str__(self):
        return self.name 
   