# Generated by Django 4.0.2 on 2022-02-09 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NotificationAPP', '0002_alter_modelnotification_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelnotification',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelnotification',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
    ]
