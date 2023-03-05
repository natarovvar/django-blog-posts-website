from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Blog
from django.contrib.auth import get_user_model


# Test for Post model
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')
    
    def test_text_content(self):
        post = Post.objects.get(id = 1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

# Test for other pages
class ForumPageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('forum'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('forum'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mb.html')

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.blog = Blog.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user,
        )

    def test_string_representation(self):
        blog = Blog(title = 'A simple title')
        self.assertEqual(str(blog),blog.title)
    
    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'A good title')
        self.assertEqual(f'{self.blog.author}', 'testuser')
        self.assertEqual(f'{self.blog.body}', 'Nice body content')
    