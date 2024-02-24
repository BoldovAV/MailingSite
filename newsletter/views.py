from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter, Letter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter')


class LetterListView(ListView):
    model = Letter


class LetterDetailView(DetailView):
    model = Letter
