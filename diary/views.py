#diary
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .models import Meal, Condition, Movement
from .forms import MealForm, ConditionForm, MovementForm
from food.models import Food
from activity.models import Activity
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext


def diary_details(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        meals = Meal.objects.all()
        movements = Movement.objects.all()
        conditions = Condition.objects.all()
        content = {
            "meals": meals,
            "movements": movements,
            "conditions": conditions
        }
        return render(request, 'diary/diary_details.html', content)
        
def diary_summary(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        meals = Meal.objects.all()
        movements = Movement.objects.all()
        conditions = Condition.objects.all()
        content = {
            "meals": meals,
            "movements": movements,
            "conditions": conditions
        }
        return render(request, 'diary/diary_summary.html', content)
        
def diary_input(request):
    return render (request, 'diary/diary_input.html')
    
def meal_input(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        form = MealForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.save()
        form = MealForm() 
        context = {
            "form": form,
        }
    return render(request, 'diary/meal_input.html', context)

def condition_input(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        form = ConditionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            condition = form.save(commit=False)
            condition.save()
        form = ConditionForm() 
        context = {
            "form": form,
        }
    return render(request, 'diary/condition_input.html', context)
    
def movement_input(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        form = MovementForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            movement = form.save(commit=False)
            movement.save()
        form = MovementForm() 
        context = {
            "form": form,
        }
    return render(request, 'diary/movement_input.html', context)