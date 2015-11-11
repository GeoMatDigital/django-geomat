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
                ('name', models.CharField(max_length=100, verbose_name='name of Handpiece')),
                ('finding_place', models.CharField(max_length=200, verbose_name='place of discovery')),
                ('current_location', models.CharField(max_length=200, verbose_name='current location')),
                ('old_inventory_number', models.CharField(max_length=100, verbose_name='old inventory number', blank=True)),
                ('resource_mindat', models.CharField(max_length=100, verbose_name='MinDat ID', blank=True)),
                ('resource_mineralienatlas', models.CharField(max_length=100, verbose_name='MineralienAtlas ID', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
        ),
        migrations.CreateModel(
            name='MineralType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trivial_name', models.CharField(max_length=100, verbose_name='trivial name')),
                ('variety', models.CharField(max_length=100, verbose_name='variety')),
                ('minerals', models.CharField(max_length=100, verbose_name='minerals')),
                ('classification', models.CharField(max_length=100, verbose_name='classification')),
                ('crystal_system', models.CharField(default=b'TC', max_length=2, verbose_name='crystal system', choices=[(b'TC', 'Triclinic'), (b'MC', 'Monoclinic'), (b'OR', 'Orthorhombic'), (b'TTG', 'Tetragonal'), (b'TRG', 'Trigonal'), (b'HG', 'Hexagonal'), (b'CB', 'Cubic')])),
                ('mohs_scale', models.CharField(max_length=20, verbose_name='mohs scale')),
                ('streak', models.CharField(max_length=100, verbose_name='streak')),
                ('normal_color', models.CharField(max_length=100, verbose_name='normal color')),
                ('fracture', models.CharField(default=b'CF', max_length=2, verbose_name='fracture', choices=[(b'CF', 'Conchoidal'), (b'EF', 'Earthy'), (b'HF', 'Hackly'), (b'SF', 'Splintery'), (b'UF', 'Uneven')])),
                ('cleavage', models.CharField(default=b'BP', max_length=2, verbose_name='cleavage', choices=[(b'BP', 'Basal/Pinacoidal'), (b'CC', 'Cubic'), (b'OC', 'Octahedral'), (b'RC', 'Rhombohedral'), (b'PM', 'Prismatic'), (b'DH', 'Dodecahedral')])),
                ('lustre', models.CharField(default=b'AM', max_length=2, verbose_name='lustre', choices=[(b'AM', 'Adamantine'), (b'DL', 'Dull'), (b'GR', 'Greasy'), (b'MT', 'Metallic'), (b'PY', 'Pearly'), (b'RS', 'Resinous'), (b'SL', 'Silky'), (b'SM', 'Submetallic'), (b'VT', 'Vitreous'), (b'WY', 'Waxy')])),
                ('chemical_formula', models.CharField(max_length=100, verbose_name='chemical formula')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
        ),
        migrations.AddField(
            model_name='handpiece',
            name='mineral_type',
            field=models.ManyToManyField(to='stein.MineralType', verbose_name='mineral type'),
        ),
    ]
