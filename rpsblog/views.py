#!/usr/bin/python
#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response,RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import Http404
from rpsblog.BlogTools import *
from rpsblog.method import *
# Create your views here.

blogt = BlogTools()
render_dict = {}
    
def artical(req,p1=1):
    p1 = int(p1)
    global blogt
    global render_dict
    recordVisiter(str(req.META['REMOTE_ADDR']))
    artlist = Article.objects.all().order_by('-createTime')
    for itm in artlist:
        if len(itm.content) > 1000:
            itm.content = itm.content[0:1500] + "..."
    render_dict = dict(blogt.getActiveTools())
    page(len(artlist),artlist,p1)
    render_dict['url'] = 'page'
    return render_to_response('blog.html',render_dict)

def page(totalartlist,artlist,p1):
    indexlist = []
    p1 = int(p1)
    totalindex = totalartlist // 4    + 1
    if p1 == 1:
        artlist = indiv_page(artlist,4,1)
        print(len(artlist))
    else:
        artlist = indiv_page(artlist,4,p1)
    for i in range(1,totalindex +1 ):
        indexlist.append(int(i))
    if p1 > 1 and p1 < int(totalindex):
        render_dict['prepage'] = int(p1 - 1)
        render_dict['nextpage'] = int(p1 + 1)
    elif p1 == 1:
        render_dict['prepage'] = int(p1)
        render_dict['nextpage'] = int(p1 + 1)
    elif p1 == totalindex:
        render_dict['nextpage'] = int(p1)
        render_dict['prepage'] = int(p1 - 1)
    render_dict['currentpage'] = int(p1)
    render_dict['article_list'] = artlist
    render_dict['index_list'] = indexlist

@ensure_csrf_cookie
def artdetail(req,p1):
    # try:
        global blogt
        global render_dict
        recordVisiter(str(req.META['REMOTE_ADDR']))
        render_dict = dict(blogt.getActiveTools())
        total = len(Article.objects.all())
        detail = Article.objects.get(id = p1)    
        artp = Article.objects.filter(id = str(int(p1) - 1))
        artn = Article.objects.filter(id = str(int(p1) + 1))
        art = Article()
        art1 = Article()
        detail.readCount += 1
        detail.save()
        if len(artp) == 0:
            art.caption = "木有了"
            art.id = p1
        else:
            art = artp[0]
        if len(artn) == 0:
            art1.id = p1
            art1.caption = "木有了" 
        else:
            art1 = artn[0]
        if detail != None:
            render_dict['artp'] = art
            render_dict['artn'] = art1
            render_dict['art_detail'] = detail
            return render_to_response('blogdetail.html',render_dict,context_instance=RequestContext(req))
        else:
            raise Http404
    # except Exception as e:
    #     raise Http404
    # else:
    #     pass
    # finally:
    #     pass

def artclassifiy(req,p1,p2=1):
    filter_art = Article.objects.filter(classification = p1)
    global blogt
    global render_dict
    recordVisiter(str(req.META['REMOTE_ADDR']))
    render_dict = dict(blogt.getActiveTools())
    for itm in filter_art:
        if len(itm.content) > 400:
            itm.content = itm.content[0:400] + "..."
    render_dict['article_list'] = filter_art
    page(len(filter_art),filter_art,p2)
    render_dict['url'] = 'classify/' + p1 + '/page'
    return render_to_response('blog.html',render_dict)


def arttag(req,p1):
    filter_art = Article.objects.filter(tags = p1)
    global blogt
    global render_dict
    recordVisiter(str(req.META['REMOTE_ADDR']))
    render_dict = dict(blogt.getActiveTools())
    for itm in filter_art:
        if len(itm.content) > 400:
            itm.content = itm.content[0:400] + "..."
    render_dict['article_list'] = filter_art
    return render_to_response('blog.html',render_dict)