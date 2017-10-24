# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_nac', models.IntegerField()),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('actores', models.ManyToManyField(to='gestor_peliculas.Actor')),
            ],
        ),
    ]
