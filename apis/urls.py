from django.conf.urls import patterns, url

from .views import IptablesReadandWriteView


urlpatterns = patterns('',
        url(r'^iptables/', IptablesReadandWriteView.as_view()),
        )
