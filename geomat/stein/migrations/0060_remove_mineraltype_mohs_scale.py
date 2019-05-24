# Generated by Django 2.0.2 on 2018-05-04 07:33

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0059_mineraltype_new_mohs_scale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='mohs_scale',
            field=models.CharField(max_length=20, verbose_name="mohs scale", default="")
        ),
        migrations.RemoveField(
            model_name='mineraltype',
            name='mohs_scale',
        ),
        migrations.RenameField(model_name="mineraltype", old_name="new_mohs_scale", new_name="mohs_scale")

    ]