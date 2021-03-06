# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 09:14


from django.db import migrations


def eliminate_hyphen_in_variety(apps, schema_editor):
    """This operation elminates hypen-corrupted fields"""
    mineral_type = apps.get_model("stein", "MineralType")
    for m in mineral_type.objects.filter(variety__contains="-").all():
        m.variety = ""
        m.save()


def revert(apps, schema_editor):
    """We do not want to revert this process, so we provide an empty revert function """
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('stein', '0034_merge_20171018_1737'),
    ]

    operations = [
        migrations.RunPython(eliminate_hyphen_in_variety, revert)

    ]

#test
