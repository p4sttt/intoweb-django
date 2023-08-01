from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        new_user = User.objects.create_user(
            username=username, email=email, password=password)
        auth_login(request, new_user)
        messages.success(request, 'Account was successfully created')
        return redirect('blog/feed')

    context = {
        'title': 'Register'
    }

    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('blog/feed')
        else:
            messages.error(request,
                           'User registration error, check password or username')

    context = {
        'title': 'Login'
    }
    return render(request, 'user/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('blog/feed')


@login_required
def profile(request):
    user = request.user
    user_posts = user.post_set.all()
    context = {
        'posts': user_posts,
        'user': user,
        'title': 'Profile'
    }

    return render(request, 'user/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user_profile = Profile.objects.filter(user=user).first()
        if 'profile-picture' in request.FILES:
            user_profile.image = request.FILES['profile-picture']
        if 'header-picture' in request.FILES:
            user_profile.banner = request.FILES['header-picture']
        if 'about' in request.POST:
            user_profile.about = request.POST['about']
        if 'status' in request.POST:
            user_profile.status = request.POST['status']
        if 'username' in request.POST:
            user.username = request.POST['username']

        user.save()
        user_profile.save()

    context = {
        'title': 'Edit profile'
    }

    return render(request, 'user/edit_profile.html', context)


def another_user_profile(request, username):
    if username == request.user.username:
        return redirect('user/profile')

    user = User.objects.filter(username=username).first()
    user_posts = user.post_set.all()
    context = {
        'posts': user_posts,
        'user': user,
        'title': user
    }
    return render(request, 'user/profile.html', context)
