# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('desactivo', 'desactivo')], default='activo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('desactivo', 'desactivo')], default='activo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('marca', models.CharField(max_length=50)),
                ('costo', models.FloatField()),
                ('precio', models.FloatField()),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('desactivo', 'desactivo')], default='activo', max_length=20)),
                ('cod_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('desactivo', 'desactivo')], default='activo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('desactivo', 'desactivo')], default='activo', max_length=20)),
                ('cod_almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Almacen')),
                ('cod_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='cod_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Proveedor'),
        ),
    ]