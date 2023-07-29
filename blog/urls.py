from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='blog/feed'),
    path('about/', views.about, name='blog/about'),
]
