# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikinciElApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]
