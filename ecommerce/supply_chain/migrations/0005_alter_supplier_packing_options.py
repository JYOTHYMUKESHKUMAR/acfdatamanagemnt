# Generated by Django 5.0 on 2024-03-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0004_supplier_initial_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='packing_options',
            field=models.CharField(choices=[('BULK', 'BULK'), ('DRUM', 'DRUM'), ('IBC', 'IBC')], default='update', max_length=50),
        ),
    ]