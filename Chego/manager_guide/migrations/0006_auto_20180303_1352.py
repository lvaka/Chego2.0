# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-03 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_guide', '0005_purveryor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='purveyor',
            field=models.CharField(choices=[(b'IFS', b'IFS'), (b'SYSCO', b'Sysco'), (b'PRODUCE', b"Nature's Produce"), (b'MEAT', b'Rocker Bros')], default='IFS', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlist',
            name='purveyor',
            field=models.CharField(choices=[(b'IFS', b'IFS'), (b'SYSCO', b'Sysco'), (b'PRODUCE', b"Nature's Produce"), (b'MEAT', b'Rocker Bros')], default='IFS', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='section',
            field=models.CharField(choices=[(b'Snacks', b'Snacks'), (b'Grill', b'Grill'), (b'Wok', b'Wok'), (b'Sweets', b'Sweets')], max_length=100),
        ),
    ]