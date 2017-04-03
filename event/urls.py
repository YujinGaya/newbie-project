from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^register$', views.register, name = 'register'),
    url(r'^events/$', views.events, name = 'events'),
    url(r'^events/(?P<event_id>[0-9]+)/$', views.event, name = 'event'),
    url(r'^$', views.index, name = 'index')
]
