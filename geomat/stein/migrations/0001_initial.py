# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handpiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name of Handpiece')),
                ('mineral_type', models.CharField(max_length=100, verbose_name='Mineral type')),
                ('finding_place', models.CharField(max_length=200, verbose_name='Place of discovery')),
                ('current_location', models.CharField(max_length=200, verbose_name='Current location')),
                ('old_inventory_number', models.CharField(max_length=100, verbose_name='Old inventory number', blank=True)),
                ('resource_mindat', models.CharField(max_length=100, verbose_name='MinDat ID')),
                ('resource_mineralienatlas', models.CharField(max_length=100, verbose_name='MineralienAtlas ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
            ],
        ),
    ]
