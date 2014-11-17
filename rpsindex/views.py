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
from rpsblog.models import *
import datetime
import time
import simplejson
from rpsindex.models import *
from rpsblog.BlogTools import *
# Create your views here.


blogt = BlogTools()
render_dict = {}

def index(req):
	global blogt
	global render_dict
	render_dict = dict(blogt.getActiveTools())
	return render_to_response('index.html',render_dict)