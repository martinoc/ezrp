# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='itemID',
            new_name='item_id',
        ),
    ]