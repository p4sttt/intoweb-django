from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.home, name='blog/home'),
    path('about/', views.about, name='blog/about'),
]
