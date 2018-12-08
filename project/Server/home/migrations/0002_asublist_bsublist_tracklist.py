# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-08 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsubList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnum', models.IntegerField(default=0)),
                ('aname', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='BsubList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnum', models.IntegerField(default=0)),
                ('bname', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TrackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=15)),
                ('tnum', models.IntegerField(default=0)),
            ],
        ),
    ]
