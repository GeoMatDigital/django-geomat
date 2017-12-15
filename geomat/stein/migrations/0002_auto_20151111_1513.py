# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='crystal_system',
            field=models.CharField(default=b'TC', max_length=2, verbose_name='crystal system', choices=[(b'TC', 'Triclinic'), (b'MC', 'Monoclinic'), (b'OR', 'Orthorhombic'), (b'TT', 'Tetragonal'), (b'TR', 'Trigonal'), (b'HG', 'Hexagonal'), (b'CB', 'Cubic')]),
        ),
    ]
