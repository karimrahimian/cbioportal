# Generated by Django 5.0.1 on 2024-02-10 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variation', '0006_remove_tissue_organ'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='organ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='variation.organ'),
        ),
    ]
