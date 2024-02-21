from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from newsletter.models import Newsletter, Letter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class LetterListView(ListView):
    model = Letter


class LetterDetailView(DetailView):
    model = Letter
