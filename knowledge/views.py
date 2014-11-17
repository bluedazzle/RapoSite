from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django import template
import time,datetime
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
import datetime
import time
import simplejson
from knowledge.models import *
# Create your views here.


def know(req):
	knowlist = KnowLib.objects.all()
	return render_to_response('knowledge.html',{'know_list':knowlist})

def req(req,p1):
	filterlist = KnowLib.objects.filter(requirement = p1)
	return render_to_response('knowledge.html',{'know_list':filterlist})
