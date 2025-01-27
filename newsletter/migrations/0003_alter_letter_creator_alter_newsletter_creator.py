# Generated by Django 4.2 on 2024-02-25 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletter', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='creator',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель письма'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='creator',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель рассылки'),
        ),
    ]
