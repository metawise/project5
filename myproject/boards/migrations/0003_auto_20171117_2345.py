# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 23:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20171117_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='last_update',
        ),
        migrations.AddField(
            model_name='topic',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]