# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0004_auto_20151111_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineraltype',
            name='lustre',
            field=models.CharField(default='AM', max_length=2, verbose_name='lustre', choices=[('AM', 'Adamantine'), ('DL', 'Dull'), ('GR', 'Greasy'), ('MT', 'Metallic'), ('PY', 'Pearly'), ('SL', 'Silky'), ('SM', 'Submetallic'), ('VT', 'Vitreous'), ('WY', 'Waxy')]),
        ),
    ]
