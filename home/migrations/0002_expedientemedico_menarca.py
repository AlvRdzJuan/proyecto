# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 03:03
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedientemedico',
            name='menarca',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Menarca', 'Menarca'), ('Ninguna', 'Ninguna')], max_length=15),
        ),
    ]
