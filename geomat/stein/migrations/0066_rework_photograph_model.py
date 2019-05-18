# Generated by Django 2.0.7 on 2019-05-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0065_delete_old_systematics_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photograph',
            name='orientation',
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='shot_type',
        ),
        migrations.AddField(
            model_name='photograph',
            name='audio_file',
            field=models.FileField(null=True, upload_to='audio', verbose_name='audio file'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='description',
            field=models.TextField(default='', verbose_name='description'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='orig_height',
            field=models.IntegerField(default=0, verbose_name='original height'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='orig_width',
            field=models.IntegerField(default=0, verbose_name='original width'),
        ),
    ]