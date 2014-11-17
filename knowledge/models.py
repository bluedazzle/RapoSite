from django.db import models
from rpsblog.models import *
# Create your models here.

class Requires(models.Model):
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class KnowLib(models.Model):
	question = models.CharField(max_length=20)
	subcaption = models.CharField(max_length=50,blank=True)
	solve = models.TextField(max_length=490)
	read = models.IntegerField(default=0)
	up = models.IntegerField(default=0)
	requirement = models.ManyToManyField(Requires)
	down = models.IntegerField(default=0)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question


