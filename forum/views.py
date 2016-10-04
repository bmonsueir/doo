#forum
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .models import Forum
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext

def forum(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        all_forum = Forum.objects.all()[:25]
        context = {
            'all_forum': all_forum
        }

        context = {
            'all_forum': all_forum,
        }
        
        return render(request, 'forum/forum.html', context)