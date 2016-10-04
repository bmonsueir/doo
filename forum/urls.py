# forum
from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns = [
 
    url(r'^(?P<forum_id>[0-9]+)/$', views.forum, name ='forum'),
    url(r'^$', views.forum, name='forum'),
]