# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=30, verbose_name='Nome do Curso')),
                ('sigla_curso', models.CharField(max_length=50, verbose_name='Sigla do Curso')),
                ('coordenador', models.CharField(max_length=50, verbose_name='Coordenador')),
            ],
        ),
    ]
