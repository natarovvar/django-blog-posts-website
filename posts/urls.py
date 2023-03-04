from django.urls import path
from . import views


urlpatterns = [
    
    path('forum/', views.MessageBoardPageView.as_view(), name = 'forum'),
]