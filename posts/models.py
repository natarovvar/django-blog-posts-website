from django.db import models
from django.urls import reverse

class Post(models.Model):
    text = models.TextField()
    


    def __str__(self):
        return self.text[:50]

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args = [str(self.id)])
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('forum')