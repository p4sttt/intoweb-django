from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='blog/feed'),
    path('about/', views.about, name='blog/about'),
    path('feed/new', views.create_post, name='blog/feed/new')
]
