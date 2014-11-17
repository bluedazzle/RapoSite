from django.conf.urls import patterns, include, url
from mycomment.views import *
urlpatterns = patterns('',
	url(r'^$',mycomment),)