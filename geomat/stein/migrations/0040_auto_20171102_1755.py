# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0039_change_fractures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizanswer',
            name='feedback_correct',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='feedback if answered correctly'),
        ),
        migrations.AlterField(
            model_name='quizanswer',
            name='feedback_incorrect',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='feedback if answered incorrectly'),
        ),
    ]