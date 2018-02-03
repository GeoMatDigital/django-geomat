# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0003_photograph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='cleavage',
            field=models.CharField(default='BP', max_length=2, verbose_name='cleavage', choices=[('PE', 'Perfect'), ('LP', 'Less perfect'), ('GO', 'Good'), ('DI', 'Distinct'), ('ID', 'Indistinct'), ('NO', 'None')]),
        ),
    ]
