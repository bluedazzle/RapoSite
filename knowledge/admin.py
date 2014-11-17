from django.contrib import admin
from knowledge.models import *
# Register your models here.

class KnowLibAdmin(admin.ModelAdmin):
	list_display = ('question','subcaption','solve','up','down','time')
	order_by = ('-time',)

class RequireAdmin(admin.ModelAdmin):
	list_display = ('title','content')

admin.site.register(KnowLib,KnowLibAdmin)
admin.site.register(Requires,RequireAdmin)