# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0005_auto_20151111_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='handpiece',
            options={'verbose_name': 'Handpiece', 'verbose_name_plural': 'Handpieces'},
        ),
        migrations.AlterModelOptions(
            name='mineraltype',
            options={'verbose_name': 'mineral type', 'verbose_name_plural': 'mineral types'},
        ),
        migrations.AlterModelOptions(
            name='photograph',
            options={'verbose_name': 'Photograph', 'verbose_name_plural': 'Photographs'},
        ),
        migrations.AlterField(
            model_name='handpiece',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name of handpiece'),
        ),
    ]
