from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, send_email_task
import redis
from django.core.cache import cache


r = redis.Redis(host='localhost', port=6379, db=1)


def index(request):
    #sleepy(10) old one without celery without async
    #sleepy.delay(10)
    #send_email_task()
    send_email_task.delay()
    return HttpResponse("email sent with celery!")


def redis(request):
    r.set('foo', 'bar')
    r_value = r.get('foo')
    r_value2 = r.get('demo3')
    cache.set("greeting", "hello", 30)
    r3_value = cache.get("greeting")

    context = {
        'foo': r_value,
        'demo3': r_value2,
        'greeting': r3_value
    }
    return render(request, 'redis.html', context)