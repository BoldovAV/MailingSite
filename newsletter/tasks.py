from datetime import datetime, timedelta

from django.core.mail import send_mail, BadHeaderError

from curse import settings
from curse.celery import app
from newsletter.models import Newsletter, Mail_log


@app.task(bind=True, ignore_result=True)
def mail_process(*args, **kwargs):
    print('Hello world21!')
    need_send = check_newsletter_status()
    print('Hello world!')
    if len(need_send) > 0:
        for news in need_send:
            recipient_list = [client.email for client in news.recipient.all()]
            print(recipient_list)
            letter_list = list(news.letter_set.all())
            for letter in letter_list:
                try:
                    send_mail(
                        subject=letter.name_letter,
                        message=letter.text_letter,
                        recipient_list=recipient_list,
                        from_email=settings.EMAIL_ADMIN
                    )
                    letter.last_try = datetime.now()
                    letter.save()
                    Mail_log.objects.create(status_try=200, answer_server='OK')
                except BadHeaderError as err:
                    Mail_log.objects.create(status_try=500, answer_server=str(err))
                except ValueError as err:
                    Mail_log.objects.create(status_try=400, answer_server=str(err))


def check_newsletter_status():
    current_datetime = datetime.now()
    current_day_delta = timedelta(days=current_datetime.day)
    current_time_delta = timedelta(hours=current_datetime.hour, minutes=current_datetime.minute)
    print('мы тут')
    newsletter_all = Newsletter.objects.filter(
        status__in=[0, 1],
        is_active=True
    )
    print(newsletter_all)
    print('и мы тут')
    need_send = []
    print(need_send)
    for news in newsletter_all:
        send_time = timedelta(hours=news.time_to_send.hour, minutes=news.time_to_send.minute)
        need_time = 0 < (send_time - current_time_delta).total_seconds() < 60
        need_date = news.period_start <= current_datetime.date() <= news.period_fin
        if need_date and news.period == 'раз в минуту (на тесты)' and news.status == 1:
            need_send.append(news)
        if need_date and news.status == 0:
            news.status = 1
            news.save()
        if need_time and need_date:
            if (news.period == 'раз в день' and
                    (current_datetime - timedelta(days=news.last_try.day) / 86400) == 1):
                need_send.append(news)
            elif (news.period == 'раз в неделю' and
                  (current_datetime - timedelta(days=news.last_try.day) / 86400) == 7):
                need_send.append(news)
            elif (news.period == 'раз в месяц' and
                  (current_day_delta - timedelta(days=news.last_try.day) / 86400) == 30):
                need_send.append(news)
        elif (news.time_to_send < current_datetime.time() and
              news.period_fin <= current_datetime.date()):
            news.status = 2
            news.save()
    return need_send
