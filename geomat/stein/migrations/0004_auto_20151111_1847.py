# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0003_photograph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='cleavage',
            field=models.CharField(default=b'BP', max_length=2, verbose_name='cleavage', choices=[(b'PE', 'Perfect'), (b'LP', 'Less perfect'), (b'GO', 'Good'), (b'DI', 'Distinct'), (b'ID', 'Indistinct'), (b'NO', 'None')]),
        ),
    ]
