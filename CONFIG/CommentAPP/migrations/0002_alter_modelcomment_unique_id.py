# Generated by Django 4.0.2 on 2022-02-08 14:11

import CommentAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommentAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcomment',
            name='unique_id',
            field=models.CharField(blank=True, default=CommentAPP.models.create_new_ref_number, editable=False, max_length=10, unique=True),
        ),
    ]
