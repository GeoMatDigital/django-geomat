# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stein', '0006_auto_20151115_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineraltype',
            name='cleavage2',
            field=models.CharField(blank=True, choices=[(b'PE', 'Perfect'), (b'LP', 'Less perfect'), (b'GO', 'Good'),
                                                        (b'DI', 'Distinct'), (b'ID', 'Indistinct'), (b'NO', 'None')],
                                   max_length=2, verbose_name='cleavage 2'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='density',
            field=models.CharField(default=0, max_length=20, verbose_name='density'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='fracture2',
            field=models.CharField(blank=True, choices=[(b'CF', 'Conchoidal'), (b'EF', 'Earthy'), (b'HF', 'Hackly'),
                                                        (b'SF', 'Splintery'), (b'UF', 'Uneven')], max_length=2,
                                   verbose_name='fracture 2'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='lustre2',
            field=models.CharField(blank=True, choices=[(b'AM', 'Adamantine'), (b'DL', 'Dull'), (b'GR', 'Greasy'),
                                                        (b'MT', 'Metallic'), (b'PY', 'Pearly'), (b'SL', 'Silky'),
                                                        (b'SM', 'Submetallic'), (b'VT', 'Vitreous'), (b'WY', 'Waxy')],
                                   max_length=2, verbose_name='lustre 2'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='other',
            field=models.CharField(blank=True, max_length=100, verbose_name='other'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='resource_mindat',
            field=models.CharField(blank=True, max_length=100, verbose_name='MinDat ID'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='resource_mineralienatlas',
            field=models.CharField(blank=True, max_length=100, verbose_name='MineralienAtlas ID'),
        ),
        migrations.AddField(
            model_name='mineraltype',
            name='systematics',
            field=models.CharField(
                choices=[(b'EL', 'Elements'), (b'SF', 'Sulfides & Sulfosalts'), (b'HG', 'Halogenides'),
                         (b'OH', 'Oxides and Hydroxides'), (b'CN', 'Carbonates and Nitrates'), (b'BR', 'Borates'),
                         (b'SL', 'Sulfates'), (b'PV', 'Phosphates, Arsenates & Vanadates'),
                         (b'SG', 'Silicates & Germanates'), (b'OC', 'Organic Compounds')], default=b'EL', max_length=2,
                verbose_name='systematics'),
        ),
        migrations.AlterField(
            model_name='handpiece',
            name='current_location',
            field=models.CharField(blank=True, max_length=200, verbose_name='current location'),
        ),
        migrations.AlterField(
            model_name='handpiece',
            name='finding_place',
            field=models.CharField(blank=True, max_length=200, verbose_name='place of discovery'),
        ),
        migrations.AlterField(
            model_name='mineraltype',
            name='crystal_system',
            field=models.CharField(blank=True,
                                   choices=[(b'TC', 'Triclinic'), (b'MC', 'Monoclinic'), (b'OR', 'Orthorhombic'),
                                            (b'TT', 'Tetragonal'), (b'TR', 'Trigonal'), (b'HG', 'Hexagonal'),
                                            (b'CB', 'Cubic')], max_length=2, verbose_name='crystal system'),
        ),
        migrations.AlterField(
            model_name='mineraltype',
            name='minerals',
            field=models.CharField(blank=True, max_length=100, verbose_name='minerals'),
        ),
        migrations.AlterField(
            model_name='mineraltype',
            name='trivial_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='trivial name'),
        ),
        migrations.AlterField(
            model_name='mineraltype',
            name='variety',
            field=models.CharField(blank=True, max_length=100, verbose_name='variety'),
        ),
    ]