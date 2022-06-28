from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, send_email_task

def index(request):
    #sleepy(10) old one without celery without async
    #sleepy.delay(10)
    #send_email_task()
    send_email_task.delay()
    return HttpResponse("email sent with celery!")