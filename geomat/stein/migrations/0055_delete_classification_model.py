# Generated by Django 2.0.2 on 2018-02-03 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0054_delete_classification_relation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classification',
        ),
    ]