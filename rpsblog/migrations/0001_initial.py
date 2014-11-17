# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=50)),
                ('capPic', models.ImageField(default=b'templates/images/default_title.jpg', upload_to=b'templates/images/')),
                ('subcaption', models.CharField(max_length=30, blank=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('readCount', models.IntegerField(default=0)),
                ('commitsCount', models.IntegerField(default=0)),
                ('updateTime', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=50000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atype', models.CharField(max_length=1)),
                ('detail', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ManyToManyField(to='rpsblog.ArticleType'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('website', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='rpsblog.Author'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cName', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='classification',
            field=models.ForeignKey(to='rpsblog.Classification'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagName', models.CharField(max_length=20)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='rpsblog.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Visiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20)),
                ('location', models.CharField(default=b'\xe7\xbd\x91\xe5\x8f\x8b', max_length=20)),
                ('times', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
