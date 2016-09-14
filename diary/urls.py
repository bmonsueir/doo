# diary
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
  
    url(r'^diary_input', views.diary_input, name ='diary_input'),
    url(r'^diary_summary', views.diary_summary, name ='diary_summary'),
]