#!/usr/bin/python
#-*- coding: UTF-8 -*-
from django.db import models
# Create your models here.
class Tag(models.Model):
    tagName = models.CharField(max_length=20)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tagName

class Visiter(models.Model):
    ip = models.CharField(max_length=20)
    location = models.CharField(max_length=20, default="网友")
    times = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

class Link(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

class Classification(models.Model):
    cName = models.CharField(max_length=30)

    def __str__(self):
        return self.cName

class ArticleType(models.Model):
    atype = models.CharField(max_length=1)
    detail = models.CharField(max_length=10)

    def __str__(self):
        return self.detail

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    caption = models.CharField(max_length=50)
    capPic = models.ImageField(max_length=100,upload_to = 'templates/images/', default = 'templates/images/default_title.jpg')
    subcaption = models.CharField(max_length=30,blank=True)
    createTime = models.DateTimeField(auto_now_add=True)
    readCount = models.IntegerField(default=0)
    commitsCount = models.IntegerField(default=0)
    updateTime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag,blank=True)
    types = models.ManyToManyField(ArticleType)
    classification = models.ForeignKey(Classification)
    content = models.CharField(max_length=50000)

    def __str__(self):
        return self.caption

