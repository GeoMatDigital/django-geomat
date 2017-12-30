# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0002_auto_20151111_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'', verbose_name='image file')),
                ('orientation', models.CharField(max_length=1, verbose_name='orientation', choices=[(b'T', 'Top'), (b'B', 'Bottom'), (b'S', 'Side')])),
                ('shot_type', models.CharField(max_length=2, verbose_name='shot type', choices=[(b'MI', 'Micro'), (b'MA', 'Macro'), (b'FE', 'Fisheye'), (b'TL', 'Tele')])),
                ('online_status', models.BooleanField(default=False, verbose_name='active photograph?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('handpiece', models.ForeignKey(to='stein.Handpiece', on_delete=models.CASCADE)),
            ],
        ),
    ]
