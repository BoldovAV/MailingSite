from django.contrib import admin

from newsletter.models import Newsletter, Client, Letter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_to_send', 'period_start', 'period_fin', 'status')
    list_filter = ('time_to_send',)
    search_fields = ('status',)
    readonly_fields = ('status',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'second_name', 'last_name', 'comment')
    list_filter = ('last_name',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('name_letter', 'text_letter')
    list_filter = ('name_letter',)
