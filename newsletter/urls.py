from django.urls import path

from newsletter.views import (NewsletterListView, NewsletterDetailView, NewsletterCreateView,
                              LetterListView, LetterDetailView, NewsletterUpdateView, NewsletterDeleteView)
from newsletter.apps import NewsletterConfig


app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter'),
    path('newsletter_detail/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/update/<int:pk>', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/delete/<int:pk>', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('letter/', LetterListView.as_view(), name='letter'),
    path('letter_detail/<int:pk>/', LetterDetailView.as_view(), name='letter_detail'),
]
