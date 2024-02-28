from django.urls import path

from newsletter.views import (NewsletterListView, NewsletterDetailView, NewsletterCreateView,
                              LetterListView, LetterDetailView, NewsletterUpdateView, NewsletterDeleteView,
                              newsletter_deactivate, LetterCreateView, LetterUpdateView, LetterDeleteView, ClientListView, ClientDetailView,
                              ClientCreateView, ClientUpdateView, ClientDeleteView)
from newsletter.apps import NewsletterConfig


app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter'),
    path('newsletter_detail/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/update/<int:pk>', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/delete/<int:pk>', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('<int:pk>/', newsletter_deactivate, name='newsletter_deactivate'),
    path('letter/', LetterListView.as_view(), name='letter'),
    path('letter_detail/<int:pk>/', LetterDetailView.as_view(), name='letter_detail'),
    path('letter/create/', LetterCreateView.as_view(), name='letter_create'),
    path('letter/update/<int:pk>', LetterUpdateView.as_view(), name='letter_update'),
    path('letter/delete/<int:pk>', LetterDeleteView.as_view(), name='letter_delete'),
    path('client/', ClientListView.as_view(), name='client'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
