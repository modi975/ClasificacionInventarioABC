# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cod_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cod_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Proveedor', verbose_name='Proveedor'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cod_almacen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Almacen', verbose_name='Almacen'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cod_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto', verbose_name='Producto'),
        ),
    ]
