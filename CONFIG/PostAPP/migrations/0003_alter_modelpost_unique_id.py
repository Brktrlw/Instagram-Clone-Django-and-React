# Generated by Django 4.0.2 on 2022-02-08 14:10

import PostAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostAPP', '0002_alter_modelpost_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelpost',
            name='unique_id',
            field=models.CharField(default=PostAPP.models.create_new_ref_number, editable=False, max_length=30, unique=True),
        ),
    ]
