from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from newsletter.forms import NewsletterForm, LetterForm, ClientForm
from newsletter.models import Newsletter, Letter, Client


# Контроллеры рассылок

class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class NewsletterListView(PermissionRequiredMixin, ListView):
    model = Newsletter
    permission_required = 'newsletter.view_all_newsletter'


class NewsletterDetailView(DetailView):
    model = Newsletter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = self.object.recipient.all()
        return context


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:newsletter')


def newsletter_deactivate(request, pk):
    newsletter_item = get_object_or_404(Newsletter, pk=pk)
    if newsletter_item.is_active:
        newsletter_item.is_active = False
    else:
        newsletter_item.is_active = True

    newsletter_item.save()
    return redirect(reverse('newsletter:newsletter'))


# Контроллеры писем

class LetterCreateView(CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('newsletter:letter')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class LetterListView(ListView):
    model = Letter


class LetterDetailView(DetailView):
    model = Letter


class LetterUpdateView(UpdateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('newsletter:letter')


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('newsletter:letter')


# Контроллеры пользователей

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:client')
