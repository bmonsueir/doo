from django import forms


from .models import Food, Method, Nutrition


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['name', 'description', 'code', 'group']


class TestForm(forms.ModelForm):

    class Meta:
        model = Method
        fields = ['name', 'abrev', 'code', 'unit']
        
        
class NutritionForm(forms.ModelForm):

    class Meta:
        model = Nutrition
        fields = ['food', 'test', 'value']
        
