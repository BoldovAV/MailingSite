from django import forms

from newsletter.forms import StyleForMixin

from blog.models import Blog


class BlogForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('name', 'message', 'preview',)
