# diary
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
  
    url(r'^diary_input', views.diary_input, name ='diary_input'),
    url(r'^diary_summary', views.diary_summary, name ='diary_summary'),
    url(r'^diary_details', views.diary_details, name ='diary_details'),
    url(r'^movement_input', views.movement_input, name ='movement_input'),
    url(r'^condition_input', views.condition_input, name ='condition_input'),
    url(r'^meal_input', views.meal_input, name ='meal_input'),
]