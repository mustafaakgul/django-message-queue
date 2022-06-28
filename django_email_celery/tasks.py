from celery import shared_task

from time import sleep

from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(8)
    send_mail("celery task worked", "celery task worked", "mustafaakgul@fastmail.com", ['gagiva5378@lankew.com'])
    return None