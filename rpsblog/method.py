from rpsblog.models import *
import os
import datetime


def recordVisiter(ip):
	vis = Visiter.objects.filter(ip = ip)
	if len(vis) > 0:
		vis[0].times += 1
		vis[0].save()
	else:
		newvis = Visiter()
		newvis.ip = ip
		newvis.save()
	return True

def indiv_page(alllist,onepage,index):
	onepage = int(onepage)
	index = int(index)
	listlen = len(alllist)
	pages = ( listlen // onepage ) + 1
	start = onepage * (index - 1)
	end = start + onepage
	if end > listlen:
		return alllist[start:]
	return alllist[start:end]
