from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import BlogForm
from .models import Post
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext

def blog(request):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        all_post = Post.objects.all()[:25]
        context = {
            'all_post': all_post
        }
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        form = BlogForm() 
        context = {
            "form": form,
            'all_post': all_post,
        }
        
        return render(request, 'blog/blog.html', context)
        
def post(request, post_id):
    if not request.user.is_authenticated():
        return render(request, 'intro/login.html')
    else:
        post = get_object_or_404(Post, id = post_id)
        content = {
            'post_title': post.title,
            'post_body': post.body,
            'post_date': post.date,
            'post_user': post.user
        }
        print(post)
    return render(request, 'blog/post.html', content)

def add(request):
    all_post = Post.objects.all()[:25]
    context = {
        'all_post': all_post
    }
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    form = BlogForm() 
    context = {
        "form": form,
        'all_post': all_post,
    }
    
    return render(request, 'blog/blog.html', context)    
    