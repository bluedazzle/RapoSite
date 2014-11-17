from django.contrib import admin
from rpsblog.models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)
            
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'subcaption', 'classification', 'author', 'createTime', 'updateTime')
    list_filter = ('createTime',)
    date_hierarchy = 'createTime'
    ordering = ('-createTime',)
    filter_horizontal = ('tags',)

class LinkAdmin(admin.ModelAdmin):
	list_display = ('name','url','email','time')
	ordering = ('-time',)

class VisiterAdmin(admin.ModelAdmin):
	list_display = ('ip','location','times','time')
	ordering = ('-time',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Visiter,VisiterAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Classification)
admin.site.register(ArticleType)