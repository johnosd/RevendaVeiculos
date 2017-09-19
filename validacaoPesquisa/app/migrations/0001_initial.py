# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 17:36
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('ano', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000)])),
                ('valor', models.FloatField()),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime(2017, 9, 3, 14, 36, 57, 622634))),
            ],
        ),
    ]
