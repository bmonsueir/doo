# blog
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
 
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name ='post'),
    url(r'^$', views.blog, name='blog'),
]
# urlpatterns = [
#     url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
#     url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name='blog/post.html')),

# ]