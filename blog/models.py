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
        
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField( max_length=255, )
    date = models.DateTimeField('date created', default=datetime.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.text
        
class Photo(models.Model):
    post = models.ForeignKey(Post)
    pic = models.ImageField(upload_to ='images')
    
class Video(models.Model):
    post = models.ForeignKey(Post)
    vid = models.FileField(upload_to = 'videos')
    
