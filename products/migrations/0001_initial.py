# Generated by Django 5.0.6 on 2024-06-27 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.unit')),
            ],
        ),
        migrations.CreateModel(
            name='ProductWarehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Buy price')),
                ('buy_price_usd', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Buy price $')),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sell price')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.warehouse')),
            ],
        ),
    ]
