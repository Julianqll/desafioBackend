# Generated by Django 5.0.2 on 2024-03-04 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_itemcompra_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcompra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='portal.producto'),
        ),
    ]
