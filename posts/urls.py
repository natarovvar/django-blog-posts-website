from django.urls import path
from . import views


urlpatterns = [
    
   # path('forum/', views.MessageBoardPageView.as_view(), name = 'forum'),
    path('forum/', views.BlogListView.as_view(), name = 'forum'), 
    path('forum/<int:pk>/',views.BlogDetailView.as_view(), name = 'blog_detail'),
]