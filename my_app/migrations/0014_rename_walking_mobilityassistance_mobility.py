# Generated by Django 5.0.6 on 2024-06-28 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_remove_mobilityassistance_date_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilityassistance',
            old_name='walking',
            new_name='mobility',
        ),
    ]
