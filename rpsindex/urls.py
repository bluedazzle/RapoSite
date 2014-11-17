from rpsindex import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.views.generic import RedirectView 
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = patterns('',
	url(r'^$',views.index),)