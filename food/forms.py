from django import forms
from django.contrib.auth.models import User

from .models import Food, Test, Nutrition


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['name', 'description', 'code', 'group']


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['name', 'abrev', 'code', 'unit']
        
        
class NutritionForm(forms.ModelForm):

    class Meta:
        model = Nutrition
        fields = ['food', 'test', 'value']