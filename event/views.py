from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse

from event.models import Event
from django.core import serializers
from django.utils import timezone
import urllib.request, json

def index(request):
    return render(request, 'index.html', {
        'lang': 'kr',
        'another': 'ab'
    })

def register(request):
    context = {}
    template = loader.get_template('register.html')

    return HttpResponse(template.render(context, request))

def events(request):
    if request.method == 'GET':
        now = timezone.now()
        events = serializers.serialize("json", Event.objects.all().filter(time__gte=now).order_by('time'))
        return JsonResponse(events, safe=False)

    elif request.method == 'POST':
        post_data = [
            ('secret','6LdD_AwUAAAAAJmyELZPK2Ijmy7jGYmTCUIlIItf'),
            ('response', request.POST['g-recaptcha-response']),
            ('remoteip', request.META['REMOTE_ADDR'])
        ]
        result = urllib.request.urlopen('https://www.google.com/recaptcha/api/siteverify', bytearray(urllib.parse.urlencode(post_data), 'utf-8'))
        result = result.read().decode('utf-8')
        result = json.loads(result)

        if result['success'] == True:
            newEvent = Event(
                title=request.POST['title'],
                description=request.POST['description'],
                time=request.POST['time'],
                ip=request.META['REMOTE_ADDR'],
            )
            newEvent.save()
        return HttpResponseRedirect('/')


def event(request, event_id):
    if request.method == 'PUT':
        event = get_object_or_404(Event, pk=event_id)
    elif request.method == 'DELETE':
        get_object_or_404(Event, pk=event_id).delete()


def login_init(request): # 사용자가 login 버튼을 눌렀을 때 실행합니다.
    login_url, state = client.get_login_params()
    session.put('state', state) # state 값을 session에 저장합니다.
    redirect_to(login_url) # 사용자를 login_url로 redirect 시킵니다.
