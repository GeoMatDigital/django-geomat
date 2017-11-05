# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0038_transfer_fracture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineraltype',
            name='fracture',
        ),
        migrations.AlterField(
            model_name='fracturetwo',
            name='coordinates',
            field=models.CharField(blank=True, help_text=b'Enter Coordinates as Following : {x,y,z,a} with the curly braces.', max_length=20, null=True, verbose_name='coordinates'),
        ),
        migrations.AlterField(
            model_name='fracturetwo',
            name='mineral_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fracture', to='stein.MineralType', verbose_name='mineraltype'),
        ),
        migrations.RenameModel('FractureTwo', 'Fracture'),
    ]