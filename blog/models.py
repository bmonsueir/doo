#blog
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField( max_length=255, )
    date = models.DateTimeField('date created', default=datetime.now)
    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blog: post', {'blog_id': self.id })

   
    def __str__(self):
        return self.title 
