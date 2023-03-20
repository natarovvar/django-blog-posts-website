from django.shortcuts import render
from django .views.generic import ListView, DetailView
from django .views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Blog, Comment
from django.contrib.auth.mixins import LoginRequiredMixin

# class MessageBoardPageView(ListView):
#    model = Post
#   template_name = 'mb.html'

class BlogListView(ListView):
    model = Blog
    template_name = 'mb.html'

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'detail'
    login_url = 'login'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'post_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']

    

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('forum')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'new_comment.html'
    fields = ['blog', 'comment']
    success_url = reverse_lazy('forum')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




