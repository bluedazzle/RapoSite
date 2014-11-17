from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
# Create your views here.

def mycomment(req):
	return render_to_response('mycomment.html')