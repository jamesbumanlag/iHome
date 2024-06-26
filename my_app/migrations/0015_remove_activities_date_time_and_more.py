# Generated by Django 5.0.6 on 2024-06-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0014_rename_walking_mobilityassistance_mobility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='healthmonitoring',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='housekeeping',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='nutritionhydration',
            name='date_time',
        ),
        migrations.AddField(
            model_name='activities',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='activities',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
        migrations.AddField(
            model_name='healthmonitoring',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='healthmonitoring',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
        migrations.AddField(
            model_name='housekeeping',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='housekeeping',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
        migrations.AddField(
            model_name='nutritionhydration',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='nutritionhydration',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
    ]
