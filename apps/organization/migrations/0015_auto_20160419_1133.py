# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0014_auto_20160412_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_bhv',
            field=models.BooleanField(default=False, help_text='Designates that this user has a valid, non-expired BHV (Emergency Response Officer) certificate.', verbose_name='has BHV-certificate'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_iva',
            field=models.BooleanField(default=False, help_text='Override for an user to indicate IVA rights without uploading a certificate.', verbose_name='has IVA-certificate'),
        ),
    ]