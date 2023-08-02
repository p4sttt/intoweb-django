from django.shortcuts import render, redirect
from django.templatetags.static import static
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


def feed(request):
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


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        categories = request.POST.getlist('category')

        categories_models_list = [Category.objects.filter(
            name=category_name).first() for category_name in categories]

        created_post = Post(author=request.user, title=title, text=text)
        created_post.save()
        created_post.categories.add(*categories_models_list)

        messages.success(request, "Post was successfully published")

        return redirect('blog/feed')

    categories = Category.objects.filter(~Q(name='default'))
    context = {
        'title': 'Create post',
        'categories': categories
    }

    return render(request, 'blog/create_post.html', context)
