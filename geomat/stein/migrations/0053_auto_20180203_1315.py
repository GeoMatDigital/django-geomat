# Generated by Django 2.0.2 on 2018-02-03 12:15

from django.db import migrations, models


def transfer_classification(apps, schema_editor):
    MineralType = apps.get_model("stein", "MineralType")

    for mineral in MineralType.objects.all().prefetch_related("classification"):

        if not mineral.classification :
            continue

        if mineral.classification.classification_name == "Doppelkettensilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "DS"
            mineral.save()

        if mineral.classification.classification_name == "Gerüstsilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "FS"
            mineral.save()

        if mineral.classification.classification_name == "Gruppensilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "GS"
            mineral.save()

        if mineral.classification.classification_name == "Hydroxid":
            mineral.split_systematics = "HY"
            mineral.save()

        if mineral.classification.classification_name == "Inselsilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "IS"
            mineral.save()

        if mineral.classification.classification_name == "Karbonat":
            mineral.split_systematics = "CA"
            mineral.save()

        if mineral.classification.classification_name == "Kettensilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "CS"
            mineral.save()

        if mineral.classification.classification_name == "Oxid":
            mineral.split_systematics = "OX"
            mineral.save()

        if mineral.classification.classification_name == "Phosphat":
            mineral.split_systematics = "PH"
            mineral.save()

        if mineral.classification.classification_name == "Ringsilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "CC"
            mineral.save()

        if mineral.classification.classification_name == "Schichtsilikat":
            mineral.split_systematics = "SI"
            mineral.sub_systematics = "PS"
            mineral.save()

        if mineral.classification.classification_name == "Sulfid":
            mineral.split_systematics = "SU"
            mineral.save()


def revert(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0052_auto_20180201_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='split_systematics',
            field=models.CharField(blank=True, choices=[('SU', 'Sulfides'), ('SS', 'Sulfosalts'), ('CA', 'Carbonates'), ('NI', 'Nitrates'), ('PH', 'Phosphates'), ('AR', 'Arsenates'), ('VA', 'Vanadates'), ('SI', 'Silicates'), ('GE', 'Germanates'), ('OX', 'Oxides'), ('HY', 'Hydroxides')], max_length=2, verbose_name='splitted systematics'),
        ),
        migrations.RunPython(transfer_classification, revert)
    ]
