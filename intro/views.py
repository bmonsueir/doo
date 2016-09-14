#intro
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
# from .forms import ChemicalForm, SpecificationForm, AttributeForm
# from .models import Chemical, Specification, Attribute
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext
from .forms import UserForm

def home(request):
    return render(request, 'intro/home.html')
    
def about(request):
    return render(request, 'intro/about.html')
    
def tutorial(request):
    return render(request, 'intro/tutorial.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'intro/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # all_project = Project.objects.filter(user=request.user)
                return render(request, 'intro/home.html')
            else:
                return render(request, 'intro/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'intro/login.html', {'error_message': 'Invalid login'})
    return render(request, 'intro/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # chemical = Chemical.objects.filter(user=request.user)
                return render(request, 'intro/home.html')
    context = {
        "form": form,
    }
    return render(request, 'intro/register.html', context)