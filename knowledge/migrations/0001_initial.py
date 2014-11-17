# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnowLib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=20)),
                ('subcaption', models.CharField(max_length=50, blank=True)),
                ('solve', models.TextField(max_length=490)),
                ('read', models.IntegerField(default=0)),
                ('up', models.IntegerField(default=0)),
                ('down', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requires',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='knowlib',
            name='requirement',
            field=models.ManyToManyField(to='knowledge.Requires'),
            preserve_default=True,
        ),
    ]
