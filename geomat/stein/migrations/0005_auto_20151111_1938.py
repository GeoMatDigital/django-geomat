# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0004_auto_20151111_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='lustre',
            field=models.CharField(default=b'AM', max_length=2, verbose_name='lustre', choices=[(b'AM', 'Adamantine'), (b'DL', 'Dull'), (b'GR', 'Greasy'), (b'MT', 'Metallic'), (b'PY', 'Pearly'), (b'SL', 'Silky'), (b'SM', 'Submetallic'), (b'VT', 'Vitreous'), (b'WY', 'Waxy')]),
        ),
    ]
