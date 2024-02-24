from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('name',)