# Generated by Django 4.0.2 on 2022-02-08 17:19

import SavedPostAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SavedPostAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelsavedpost',
            name='unique_id',
            field=models.CharField(default=SavedPostAPP.models.create_new_ref_number, editable=False, max_length=30, unique=True),
        ),
    ]
