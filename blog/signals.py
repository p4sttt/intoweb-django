from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Category, Post


@receiver(post_save, sender=Post)
def set_default_categoty(sender, instance, created, **kwargs):
    if created:
        default_category = Category.objects.filter(name='default').first()
        instance.categories.add(default_category)
