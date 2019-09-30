# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-26 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0031_delete_cgac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psc',
            name='code',
            field=models.CharField(max_length=4),
        ),
        migrations.AddField(
            model_name='psc',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='psc',
            name='full_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psc',
            name='includes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psc',
            name='excludes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psc',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psc',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psc',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        )
    ]
