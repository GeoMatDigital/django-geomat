# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 18:59


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0044_auto_20171112_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineraltype',
            name='cleavage',
        ),
        migrations.AlterField(
            model_name='cleavage',
            name='mineral_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cleavage', to='stein.MineralType', verbose_name='mineral type'),
        ),
    ]
