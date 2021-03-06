# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20170519_0621'),
        ('comprobante', '0003_detalle_ingreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Salida',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('total', models.FloatField(default=0)),
                ('cod_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto', verbose_name='Producto')),
                ('cod_salida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalle_salida', to='comprobante.Salida')),
            ],
        ),
    ]
