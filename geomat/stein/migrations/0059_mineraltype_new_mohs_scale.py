# Generated by Django 2.0.2 on 2018-05-03 18:57

from decimal import Decimal
import django.contrib.postgres.fields.ranges
from django.db import migrations


def transform_to_new_mohs_scale(apps, schema_editor):
    MineralType = apps.get_model("stein", "MineralType")

    for mineral in MineralType.objects.all():
        tpl = ()
        mohs = mineral.mohs_scale

        if not ("-" in mohs):
            mohs = float(mohs.replace(",", "."))
            tpl = (mohs, mohs + 0.001)
        else:
            tpl = tuple(float(x) for x in mohs.replace(",", ".").split("-"))

        mineral.new_mohs_scale = tpl
        mineral.save()


def revert(apps, schema_editor):
    MineralType = apps.get_model("stein", "MineralType")

    for mineral in MineralType.objects.all():

        if float(mineral.new_mohs_scale.upper) == float(mineral.new_mohs_scale.lower) + 0.001:
            mineral.mohs_scale = "{}".format(mineral.new_mohs_scale.lower).replace(".", ",")
        else:
            mineral.mohs_scale = "{0}-{1}".format(mineral.new_mohs_scale.lower,
                                                  mineral.new_mohs_scale.upper).replace(".", ",")

        mineral.save()


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0058_remove_mineraltype_density'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineraltype',
            name='new_mohs_scale',
            field=django.contrib.postgres.fields.ranges.FloatRangeField(blank=True, null=True),
        ),
        migrations.RunPython(transform_to_new_mohs_scale, revert)
    ]
