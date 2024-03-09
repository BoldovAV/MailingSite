from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта клиента')
    first_name = models.CharField(max_length=50, verbose_name='имя')
    second_name = models.CharField(max_length=50, default='-', verbose_name='отчество', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='создатель рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('last_name',)


class Newsletter(models.Model):
    class Conditions(models.IntegerChoices):
        MAKE = 0, 'создана'
        GO = 1, 'в процессе'
        FIN = 2, 'завершена'

    DAYS = 'раз в день'
    WEEK = 'раз в неделю'
    MONT = 'раз в месяц'
    MINU = 'раз в минуту (на тесты)'

    PERIOD_TYPE = (
        (DAYS, 'раз в день'),
        (WEEK, 'раз в неделю'),
        (MONT, 'раз в месяц'),
        (MINU, 'раз в минуту (на тесты)'),
    )
    name = models.CharField(max_length=50, default='без имени', verbose_name='название рассылки', **NULLABLE)
    time_to_send = models.TimeField(verbose_name='время рассылки')
    period_start = models.DateField(verbose_name='дата начала рассылки')
    period_fin = models.DateField(verbose_name='дата конца рассылки')
    period = models.CharField(max_length=25, default=MINU, choices=PERIOD_TYPE,
                              verbose_name='периодичность рассылки')
    status = models.IntegerField(choices=Conditions.choices, default=0,
                                 verbose_name='статус рассылки')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='создатель рассылки', **NULLABLE)

    recipient = models.ManyToManyField(to='Client', verbose_name='получатели', **NULLABLE)

    is_active = models.BooleanField(default=True)

    last_try = models.DateTimeField(verbose_name='дата/время последней отправки', **NULLABLE)

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('status',)
        permissions = [
            (
                'view_all_newsletter',
                'Can view all newsletter'
            )
        ]

    def __str__(self):
        return self.name


class Letter(models.Model):
    name_letter = models.CharField(max_length=100, verbose_name='тема письма')
    text_letter = models.TextField(verbose_name='текст письма')

    period_to_send = models.ManyToManyField(to='Newsletter', verbose_name='в каких рассылках')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='создатель рассылки', **NULLABLE)

    def __str__(self):
        return self.name_letter

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('name_letter',)


class Mail_log(models.Model):
    last_try = models.DateField(auto_now=True, verbose_name='дата последней попытки')
    status_try = models.PositiveIntegerField(verbose_name='статус попытки')
    answer_server = models.CharField(max_length=150, verbose_name='ответ сервера', **NULLABLE)

    def __str__(self):
        return self.last_try

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('last_try', 'status_try',)
