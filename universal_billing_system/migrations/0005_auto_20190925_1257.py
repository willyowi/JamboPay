# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-25 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universal_billing_system', '0004_merge_20190925_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='Industry',
        ),
        migrations.AddField(
            model_name='merchant',
            name='Industry',
            field=models.ManyToManyField(to='universal_billing_system.Industry'),
        ),
    ]
