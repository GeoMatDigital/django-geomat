# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 16:14


from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0019_auto_20170115_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photograph',
            name='image_file',
            field=stdimage.models.StdImageField(upload_to=''),
        ),
    ]
