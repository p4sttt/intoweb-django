from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('auth/register/', views.register, name='user/register'),
    path('auth/login/', views.login, name='user/login'),
    path('auth/logout/', views.logout, name='user/logout'),
    path('profile/', views.profile, name='user/profile'),
    path('profile/<str:username>', views.another_user_profile, name='user/profile/another_user_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
