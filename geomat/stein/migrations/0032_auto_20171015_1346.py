# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 11:46


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0031_auto_20171015_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='difficulty'),
        ),
    ]
