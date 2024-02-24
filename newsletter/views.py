from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter, Letter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(**kwargs)
    #     queryset.recipient = queryset.get(pk=self.kwargs.get('pk')).recipient.all()
    #     # recepients = queryset.get(pk=self.kwargs.get('pk'))#.recipient.all()
    #     # print(recepients)
    #     print(queryset.recipient)
    #     # print(queryset.recipient)
    #     return queryset


# {% for client in object.recipient %}
#                         {{ client }}
#                     {% endfor %}


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('name', 'time_to_send', 'period_start', 'period_fin', 'period', 'recipient',)
    success_url = reverse_lazy('newsletter:newsletter')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:newsletter')


class LetterListView(ListView):
    model = Letter


class LetterDetailView(DetailView):
    model = Letter
