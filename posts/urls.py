from django.urls import path
from . import views


urlpatterns = [
    
   # path('forum/', views.MessageBoardPageView.as_view(), name = 'forum'),
    path('forum/', views.BlogListView.as_view(), name = 'forum'), 
    path('forum/<int:pk>/',views.BlogDetailView.as_view(), name = 'blog_detail'),
    path('forum/new/',views.BlogCreateView.as_view(), name = 'post_new'),
    path('forum/<int:pk>/edit/',views.BlogUpdateView.as_view(), name = 'blog_edit'),
    path('forum/<int:pk>/delete/',views.BlogDeleteView.as_view(), name = 'blog_delete'),
]