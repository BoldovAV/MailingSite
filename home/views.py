import random

from django.shortcuts import render

from blog.models import Blog
from home.services import cache_search
from newsletter.models import Newsletter, Client


def home(request):
    blog_all = list(Blog.objects.all())
    if len(blog_all) >= 3:
        blog_list_home = random.sample(blog_all, k=3)
    elif len(blog_all) in [1, 2]:
        blog_list_home = random.sample(blog_all, k=len(blog_all))
    else:
        blog_list_home = None
    context = {
        'title': 'Хоть обрассылайся',
        'object_all': len(Newsletter.objects.all()),
        'object_is_active': cache_search(),
        'client_all': len(Client.objects.all()),
        'blog_list': blog_list_home

    }
    return render(request, 'home/home.html', context)
