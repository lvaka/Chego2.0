# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-03 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_guide', '0003_order_orderlist_purveryor'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordernumber',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]