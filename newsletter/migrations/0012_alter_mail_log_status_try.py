# Generated by Django 4.2 on 2024-03-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_newsletter_last_try'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail_log',
            name='status_try',
            field=models.PositiveIntegerField(verbose_name='статус попытки'),
        ),
    ]