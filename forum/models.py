#forum
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Forum(models.Model):
    ref = models.ForeignKey('self', on_delete=models.CASCADE)
    text = models.TextField( max_length=255, )
    date = models.DateTimeField('date created', default=datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        get_latest_by = "date"
        
    def __str__(self):
        return self.text