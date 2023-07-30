from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('blog/feed')
        else:
            messages.error(request, 'Account registration error')

    else:
        form = UserRegisterForm()

    context = {
        'form': form,
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
            messages.error(
                'User registration error, check password or username')

    context = {
        'title': 'Login'
    }
    return render(request, 'user/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('blog/feed')
