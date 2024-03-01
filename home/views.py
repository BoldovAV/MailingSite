import random

from django.shortcuts import render

from blog.models import Blog
from newsletter.models import Newsletter, Client


def home(request):
    blog_all = list(Blog.objects.all())
    blog_list_home = random.sample(blog_all, k=3)
    context = {
        'title': 'Домашняя страница',
        'object_all': len(Newsletter.objects.all()),
        'object_is_active': len(Newsletter.objects.filter(is_active=True)),
        'client_all': len(Client.objects.all()),
        'blog_list': blog_list_home

    }
    return render(request, 'home/home.html', context)
