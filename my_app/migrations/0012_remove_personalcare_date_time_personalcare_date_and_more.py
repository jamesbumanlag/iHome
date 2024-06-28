# Generated by Django 5.0.6 on 2024-06-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_activities_date_time_activities_person_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalcare',
            name='date_time',
        ),
        migrations.AddField(
            model_name='personalcare',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='personalcare',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
    ]