# Generated by Django 2.0.2 on 2018-04-25 07:44

from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0056_mineraltype_new_density'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineraltype',
            name='density',
        ),
        migrations.RenameField(model_name="mineraltype", old_name="new_density", new_name="density")
    ]