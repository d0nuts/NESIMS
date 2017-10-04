# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]