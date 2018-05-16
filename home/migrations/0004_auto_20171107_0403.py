# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_expedientemedico_archivos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientemedico',
            name='aseguranza',
            field=models.CharField(blank=True, choices=[('Banorte', 'Banorte'), ('Axxa', 'Axxa'), ('Allianz', 'Allianz'), ('GNP', 'GNP'), ('La Latino Seguros', 'La Latino Seguros'), ('MAPFRE', 'MAPFRE'), ('Metlife', 'Metlife'), ('Seguros Atlas', 'Seguros Atlas'), ('Seguros Monterrey', 'Seguros Monterrey'), ('Bupa', 'Bupa')], max_length=100),
        ),
    ]
