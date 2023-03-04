from django.shortcuts import render
from .models import Post
from django .views.generic import ListView

class MessageBoardPageView(ListView):
    model = Post
    template_name = 'mb.html'
    