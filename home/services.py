from django.core.cache import cache

from curse import settings
from newsletter.models import Newsletter


def cache_search():
    if settings.CACHE_ENABLED:
        key = 'object_is_active'
        object_is_active = cache.get(key)
        if object_is_active is None:
            object_is_active = len(Newsletter.objects.filter(is_active=True))
            cache.set(key, object_is_active)
    else:
        object_is_active = len(Newsletter.objects.filter(is_active=True))
    return object_is_active
