# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handpiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name of Handpiece')),
                ('finding_place', models.CharField(max_length=200, verbose_name='place of discovery')),
                ('current_location', models.CharField(max_length=200, verbose_name='current location')),
                ('old_inventory_number', models.CharField(max_length=100, verbose_name='old inventory number', blank=True)),
                ('resource_mindat', models.CharField(max_length=100, verbose_name='MinDat ID', blank=True)),
                ('resource_mineralienatlas', models.CharField(max_length=100, verbose_name='MineralienAtlas ID', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
        ),
        migrations.CreateModel(
            name='MineralType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trivial_name', models.CharField(max_length=100, verbose_name='trivial name')),
                ('variety', models.CharField(max_length=100, verbose_name='variety')),
                ('minerals', models.CharField(max_length=100, verbose_name='minerals')),
                ('classification', models.CharField(max_length=100, verbose_name='classification')),
                ('crystal_system', models.CharField(default='TC', max_length=2, verbose_name='crystal system', choices=[('TC', 'Triclinic'), ('MC', 'Monoclinic'), ('OR', 'Orthorhombic'), ('TTG', 'Tetragonal'), ('TRG', 'Trigonal'), ('HG', 'Hexagonal'), ('CB', 'Cubic')])),
                ('mohs_scale', models.CharField(max_length=20, verbose_name='mohs scale')),
                ('streak', models.CharField(max_length=100, verbose_name='streak')),
                ('normal_color', models.CharField(max_length=100, verbose_name='normal color')),
                ('fracture', models.CharField(default='CF', max_length=2, verbose_name='fracture', choices=[('CF', 'Conchoidal'), ('EF', 'Earthy'), ('HF', 'Hackly'), ('SF', 'Splintery'), ('UF', 'Uneven')])),
                ('cleavage', models.CharField(default='BP', max_length=2, verbose_name='cleavage', choices=[('BP', 'Basal/Pinacoidal'), ('CC', 'Cubic'), ('OC', 'Octahedral'), ('RC', 'Rhombohedral'), ('PM', 'Prismatic'), ('DH', 'Dodecahedral')])),
                ('lustre', models.CharField(default='AM', max_length=2, verbose_name='lustre', choices=[('AM', 'Adamantine'), ('DL', 'Dull'), ('GR', 'Greasy'), ('MT', 'Metallic'), ('PY', 'Pearly'), ('RS', 'Resinous'), ('SL', 'Silky'), ('SM', 'Submetallic'), ('VT', 'Vitreous'), ('WY', 'Waxy')])),
                ('chemical_formula', models.CharField(max_length=100, verbose_name='chemical formula')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
        ),
        migrations.AddField(
            model_name='handpiece',
            name='mineral_type',
            field=models.ManyToManyField(to='stein.MineralType', verbose_name='mineral type'),
        ),
    ]
