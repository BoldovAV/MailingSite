from django import forms

from newsletter.models import Newsletter, Letter


class StyleForMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ('time_to_send', 'period_start', 'period_fin', 'period', 'recipient',)
