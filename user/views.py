from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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
    if request.method != 'POST':
        context = {
            'title': 'Login'
        }
        return render(request, 'user/login.html', context)

    else:
        print("login handle")
