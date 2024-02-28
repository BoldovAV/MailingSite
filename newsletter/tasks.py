from curse.celery import app


@app.task(bind=True, ignore_result=True)
def mail_process(*args, **kwargs):
    print('Hello world!')
