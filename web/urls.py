from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('feed/')),
    path('', include('user.urls')),
    path('', include('blog.urls')),
]
