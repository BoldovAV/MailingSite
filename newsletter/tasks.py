from datetime import datetime, timedelta

from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

from curse.celery import app
from newsletter.models import Newsletter, Client, Letter, Mail_log


@app.task(bind=True, ignore_result=True)
def mail_process(*args, **kwargs):
    print('Hello world21!')
    need_send = check_newsletter_status()
    print('Hello world!')
    if len(need_send) > 0:
        for news in need_send:
            recipient_list = list(news.client_set.all().email)
            letter_list = list(news.letter_set.all())
            for letter in letter_list:
                try:
                    send_mail(
                        subject=letter.name_letter,
                        message=letter.text_letter,
                        recipient_list=recipient_list,
                    )
                    Mail_log.objects.create(status_try=200, answer_server='OK')
                except BadHeaderError as err:
                    Mail_log.objects.create(status_try=500, answer_server=str(err))
                except ValueError as err:
                    Mail_log.objects.create(status_try=400, answer_server=str(err))


def check_newsletter_status():
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    print('мы тут')
    print(type(Newsletter))
    newsletter_all = Newsletter.objects.filter(
        Q(status__in=(0, 1)),
        Q(is_active=True)
    )
    need_send = []
    for news in newsletter_all:
        if (news.time_to_send <= current_time <= (news.time_to_send + timedelta(minutes=1)).time() and
                news.period_start <= current_date <= news.period_fin):
            news.status = 1
            news.save()
            if news.period in ['MINU', 'DAYS']:
                need_send.append(news)
            elif news.period == 'WEEK':
                if ((current_date - news.period_start).days % 7) == 0:
                    need_send.append(news)
            elif news.period == 'MONT':
                if ((current_date - news.period_start).days % 30) == 0:
                    need_send.append(news)
        elif (news.time_to_send < current_time and
              news.period_fin <= current_date):
            news.status = 2
            news.save()
    return need_send

# start = datetime(2024, 2, 16).date()
# seicas = datetime.now().date()
# print(start)
# print(seicas)
# raznica = (seicas - start).days % 7
# dilim = raznica % 7
#
# print(raznica)
# print(dilim)
# print(datetime.now() + timedelta(days=7))
# print((datetime.now() + timedelta(minutes=10)).time())
# news = Newsletter.objects.all()
# print(type(news))

# (news.time_to_send + timedelta(minutes=1)).time()
