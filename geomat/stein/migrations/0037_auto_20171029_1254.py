# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0036_fracturetwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fracturetwo',
            name='mineral_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fracturetwo', to='stein.MineralType', verbose_name='mineraltype'),
        ),
    ]