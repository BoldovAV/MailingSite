from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

from blog.forms import BlogForm
from blog.models import Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    permission_required = 'blog.add_blog'
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog')


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    permission_required = 'blog.change_blog'
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog')

    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    permission_required = 'blog.delete_blog'
    success_url = reverse_lazy('blog:blog')
