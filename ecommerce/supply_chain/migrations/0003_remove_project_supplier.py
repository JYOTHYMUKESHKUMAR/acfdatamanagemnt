# Generated by Django 5.0 on 2024-03-17 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0002_supplier_supplier_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='supplier',
        ),
    ]
