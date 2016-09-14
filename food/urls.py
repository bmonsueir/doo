# food

from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^', views.food, name ='food'),
    url(r'^q=<request.GET.q>', views.search_food, name='search_food')
]