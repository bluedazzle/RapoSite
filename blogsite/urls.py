from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.views.generic import RedirectView 
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^admin/rpsblog/article/1/static/',include('DjangoUeditor.urls' )),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('rpsblog.urls')),
    url(r'^knowledge/',include('knowledge.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', include('rpsindex.urls')),
    url(r'^about/',include('about.urls')),
    url(r'^mycomment/',include('mycomment.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_DIR}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMG_DIR}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_DIR}),
)
