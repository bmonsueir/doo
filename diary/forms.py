#diary
from django import forms
from django.contrib.auth.models import User

from .models import  Meal, Condition, Movement


class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ['food', 'amount', 'description', 'timeOf']

class ConditionForm(forms.ModelForm):

    class Meta:
        model = Condition
        fields = ['health', 'weight', 'height', 'timeOf']

class MovementForm(forms.ModelForm):

    class Meta:
        model = Movement
        fields = ['name', 'amount', 'description', 'timeOf']