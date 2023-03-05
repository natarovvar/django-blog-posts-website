from django.shortcuts import render
from django .views.generic import ListView, DetailView
from django .views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('forum')

