from datetime import datetime, timedelta

from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

from curse import settings
from curse.celery import app
from newsletter.models import Newsletter, Client, Letter, Mail_log


@app.task(bind=True, ignore_result=True)
def mail_process(*args, **kwargs):
    print('Hello world21!')
    need_send = check_newsletter_status()
    print('Hello world!')
    if len(need_send) > 0:
        for news in need_send:
            # recipient_list = list(news.recipient.all())
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
    # newsletter_all = Newsletter.objects.filter(
    #     Q(status__in=(0, 1)),
    #     Q(is_active=True)
    # )
    print(newsletter_all)
    print('и мы тут')
    need_send = []
    print(need_send)
    for news in newsletter_all:
        send_time = timedelta(hours=news.time_to_send.hour, minutes=news.time_to_send.minute)
        # print(news.period)
        # print(news.period_start)
        # print(current_datetime.date())
        # print(news.period_fin)
        # print(news.period_start <= current_datetime.date() <= news.period_fin)
        # print(0 < (send_time - current_time_delta).total_seconds() < 60)

        print('первая прошла')
        need_time = 0 < (send_time - current_time_delta).total_seconds() < 60
        need_date = news.period_start <= current_datetime.date() <= news.period_fin
        if need_date and news.period == 'раз в минуту (на тесты)' and news.status == 1:
            print('Hiiii minuta')
            need_send.append(news)
        if need_date and news.status == 0:
            print(news.status)
            news.status = 1
            news.save()
            print(news.status)
        if need_time and need_date:
            # print(news.status)
            # if news.status == 0:
            #     news.status = 1
            #     news.save()
            # print(news.status)
            # if news.period == 'раз в минуту (на тесты)':
            #     print('Hiiii minuta')
            #     need_send.append(news)
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
        # elif (news.period == 'раз в минуту (на тесты)' and
        #         (news.period_start <= current_datetime.date() <= news.period_fin) and news.status == 1):
        #     print('Hiiii minuta')
        #     need_send.append(news)
    print(need_send)
    return need_send

# Старая логика:

# current_day_delta = timedelta(days=current_datetime.day)
# current_time_delta = timedelta(hours=current_datetime.hour, minutes=current_datetime.minute)


#     for news in newsletter_all:
#         send_time = timedelta(hours=news.time_to_send.hour, minutes=news.time_to_send.minute)
#         if (0 < (send_time - current_time_delta).total_seconds() < 60 and
#                 news.period_start <= current_datetime.date() <= news.period_fin):
#             news.status = 1
#             news.save()
#             if news.period in ['MINU', 'DAYS']:
#                 need_send.append(news)
#             elif news.period == 'WEEK' and (current_datetime - timedelta(news.last_try) == 7:
#                 need_send.append(news)
#             elif news.period == 'MONT' and (current_day_delta - timedelta(days=news.last_try.day)) == 0:
#                 need_send.append(news)
#             elif (news.time_to_send < current_datetime.time()) and
#                     news.period_fin <= current_datetime.date()):
#                 news.status = 2
#             news.save()


# current_date = datetime.now().date()
# current_time = datetime.now().time()

# for news in newsletter_all:
#     if (news.time_to_send <= current_time <= (news.time_to_send + timedelta(minutes=1)).time() and
#             news.period_start <= current_date <= news.period_fin):
#         news.status = 1
#         news.save()
#         if news.period in ['MINU', 'DAYS']:
#             need_send.append(news)
#         elif news.period == 'WEEK':
#             if ((current_date - news.period_start).days % 7) == 0:
#                 need_send.append(news)
#         elif news.period == 'MONT':
#             if ((current_date - news.period_start).days % 30) == 0:
#                 need_send.append(news)
#     elif (news.time_to_send < current_time and
#           news.period_fin <= current_date):
#         news.status = 2
#         news.save()


# start = datetime(2024, 2, 16, 16, 15, 00)
# start2 = datetime(2024, 2, 16, 16, 15, 00).month
# seicas = datetime.now().time()
# tm1 = timedelta(hours=start.hour, minutes=start.minute)
# tm2 = timedelta(hours=seicas.hour, minutes=seicas.minute)
# print(start)
# print(start2)
#
# print(seicas)
# raznica = (tm1 - tm2).total_seconds()/60
# # dilim = raznica % 7
#
# print(raznica)
# print(dilim)
# print(datetime.now() + timedelta(days=7))
# print((datetime.now() + timedelta(minutes=10)).time())
# news = Newsletter.objects.all()
# print(type(news))

# (news.time_to_send + timedelta(minutes=1)).time()

# seicas = datetime.now()
# datetime_some = datetime(year=2024, month=1, day=7, hour=12, minute=10, second=00)
# day_some_date = timedelta(days=datetime_some.day)
# current_day_delta = timedelta(days=seicas.day)
# current_time_delta = timedelta(hours=seicas.hour, minutes=seicas.minute)
# print(seicas)
# print((seicas - datetime_some))
# print((seicas + relativedelta(days=7)).date())
