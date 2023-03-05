from django.shortcuts import render
from django .views.generic import ListView, DetailView
from .models import Post
from .models import Blog

# class MessageBoardPageView(ListView):
#    model = Post
#   template_name = 'mb.html'

class BlogListView(ListView):
    model = Blog
    template_name = 'mb.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'detail'

