from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'preview', 'date_create', 'count_view')
    list_filter = ('count_view',)
    search_fields = ('name', 'message',)
    readonly_fields = ('date_create', 'count_view', )
