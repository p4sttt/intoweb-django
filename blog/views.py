from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from .models import Post, Category


def home(request):
    categories = [
        {
            'title': 'All',
            'icon': static('blog/icons/hash-outline.svg'),
            'category': Category.objects.filter(name="default").first()
        },
        {
            'title': 'Popular',
            'icon': static('blog/icons/fire-outline.svg'),
            'category': Category.objects.filter(name="default").first()
        },
        {
            'title': 'Design',
            'icon': static('blog/icons/color-palette-outline.svg'),
            'category': Category.objects.filter(name="design").first()
        },
        {
            'title': 'Development',
            'icon': static('blog/icons/code-outline.svg'),
            'category': Category.objects.filter(name="development").first()
        },
        {
            'title': 'Marketing',
            'icon': static('blog/icons/message-circle-outline.svg'),
            'category': Category.objects.filter(name="marketing").first()
        },
    ]
    category = request.GET.get('category')

    if not category:
        posts = Post.objects.all()
    else:
        posts = Category.objects.filter(name=category).first().post_set.all()


    context = {
        'posts': posts,
        'categories': categories,
        'category': category
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }

    return render(request, 'blog/about.html', context)
