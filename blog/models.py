from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField( max_length=255, )
    date = models.DateTimeField('date created', default=datetime.now)
    user = models.ForeignKey(User)
   
    def __str__(self):
        return self.title 
