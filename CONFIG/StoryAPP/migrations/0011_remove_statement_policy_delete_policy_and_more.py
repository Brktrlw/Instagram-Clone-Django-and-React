# Generated by Django 4.0.2 on 2022-02-17 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoryAPP', '0010_policy_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='policy',
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
        migrations.DeleteModel(
            name='Statement',
        ),
    ]
