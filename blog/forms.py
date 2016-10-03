#blog
from django import forms
from django.contrib.auth.models import User

from .models import Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']
