from django.conf.urls import patterns, include, url
from rpsblog.views import *
urlpatterns = patterns('',
	url(r'^$',artical),
	url(r'^(\d+)/$',artdetail,name = "blogdetail"),
	url(r'^classify/(\d+)/$',artclassifiy),
	url(r'^tag/(\d+)/$',arttag),
	url(r'^page/(\d+)/$',artical),
	url(r'^classify/(\d+)/page/(\d+)/$',artclassifiy),
)