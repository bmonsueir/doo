#food
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
# from .forms import ChemicalForm, SpecificationForm, AttributeForm
from .models import Food, Method, Nutrition
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext


# def food(request):
    
#     return render(request, 'food/food.html')
    
def food(request):
    item  = Food.objects.all().order_by('name')#[:10] #when you have sth to filter ;)
    form = request.POST
    q = request.GET.get('item_id')
    if request.GET:
        values = request.GET
        print ("values",values)
    print("food")
    # you can remove the preview assignment (form =request.POST)
    if request.method == 'POST':
        selected_item = get_object_or_404(Food, pk=request.POST.get('item_id'))
        print(selected_item)
    return render (request, 'food/food.html', {'items':item})

def search_food(request, q):
    item  = Food.objects.filter(q).order_by('name')#[:10] #when you have sth to filter ;)
    form = request.POST
    if request.GET:
        values = request.GET
        print (values)
    print("search_food")
    # you can remove the preview assignment (form =request.POST)
    if request.method == 'POST':
        selected_item = get_object_or_404(Food, pk=request.POST.get('item_id'))
        print(selected_item)
    return render (request, 'food/food.html', {'items':item})

