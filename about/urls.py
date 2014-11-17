from django.conf.urls import patterns, include, url
from about.views import *
urlpatterns = patterns('',
	url(r'^$',about),)