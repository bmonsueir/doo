# blog
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
 
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name ='post'),
    url(r'^$', views.blog, name='blog'),
]
