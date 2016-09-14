# intro
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name ='home'),
    url(r'^about', views.about, name ='about'),
    url(r'^tutorial', views.tutorial, name ='tutorial'),
]