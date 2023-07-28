from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

posts = [
    {
        'title': "Microsoft kinda nailed it with this one",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Microsoft"
    },
    {
        'title': "Some boring title",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Google"
    },
    {
        'title': "Hello World",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Apple"
    },
    {
        'title': "Hello World",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Apple"
    },
    {
        'title': "Hello World",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Apple"
    },
    {
        'title': "Hello World",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Apple"
    },
    {
        'title': "Hello World",
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'author': "Apple"
    },
]
categories = [
    {
        'title': 'All',
        'icon': static('blog/icons/hash-outline.svg')
    },
    {
        'title': 'Popular',
        'icon': static('blog/icons/fire-outline.svg')
    },
    {
        'title': 'Design',
        'icon': static('blog/icons/color-palette-outline.svg')
    },
    {
        'title': 'Development',
        'icon': static('blog/icons/code-outline.svg')
    },
    {
        'title': 'Marketing',
        'icon': static('blog/icons/message-circle-outline.svg')
    },
]


def home(request):
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }

    return render(request, 'blog/about.html', context)
