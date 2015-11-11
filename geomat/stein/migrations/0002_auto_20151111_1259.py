# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handpiece',
            name='resource_mindat',
            field=models.CharField(max_length=100, verbose_name='MinDat ID', blank=True),
        ),
        migrations.AlterField(
            model_name='handpiece',
            name='resource_mineralienatlas',
            field=models.CharField(max_length=100, verbose_name='MineralienAtlas ID', blank=True),
        ),
    ]
