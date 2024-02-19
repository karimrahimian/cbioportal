# Generated by Django 5.0.1 on 2024-02-13 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variation', '0007_sample_organ'),
    ]

    operations = [
        migrations.CreateModel(
            name='SNPMutant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variation.gene')),
                ('molecular_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variation.moleculeprofile')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variation.sample')),
            ],
        ),
    ]