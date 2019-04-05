# Generated by Django 2.1.7 on 2019-04-04 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0064_populate_new_systematics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineraltype',
            name='split_systematics',
        ),
        migrations.RemoveField(
            model_name='mineraltype',
            name='sub_systematics',
        ),
        migrations.RemoveField(
            model_name='mineraltype',
            name='systematics',
        ),
        migrations.RenameField(
            model_name='mineraltype', old_name="new_systematics", new_name="systematics"
        )
    ]
