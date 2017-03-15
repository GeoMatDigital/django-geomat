# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 14:24
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stein', '0007_auto_20160615_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrystalSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crystal_system', models.CharField(blank=True, choices=[(b'TC', 'Triclinic'), (b'MC', 'Monoclinic'),
                                                                         (b'OR', 'Orthorhombic'), (b'TT', 'Tetragonal'),
                                                                         (b'TR', 'Trigonal'), (b'HG', 'Hexagonal'),
                                                                         (b'CB', 'Cubic')], max_length=2,
                                                    verbose_name='crystal system')),
                ('temperature', models.IntegerField(verbose_name='temperature')),
                ('pressure', models.IntegerField(verbose_name='pressure')),
                ('mineral_type',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stein.MineralType',
                                   verbose_name='mineral type')),
            ],
        ),
    ]