# Generated by Django 4.2 on 2024-02-25 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsletter', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель рассылки'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='recipient',
            field=models.ManyToManyField(blank=True, null=True, to='newsletter.client', verbose_name='получатели'),
        ),
        migrations.AddField(
            model_name='letter',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель письма'),
        ),
        migrations.AddField(
            model_name='letter',
            name='period_to_send',
            field=models.ManyToManyField(to='newsletter.newsletter', verbose_name='в каких рассылках'),
        ),
    ]
