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
            field=models.CharField(default='TC', max_length=2, verbose_name='crystal system', choices=[('TC', 'Triclinic'), ('MC', 'Monoclinic'), ('OR', 'Orthorhombic'), ('TT', 'Tetragonal'), ('TR', 'Trigonal'), ('HG', 'Hexagonal'), ('CB', 'Cubic')]),
        ),
    ]
