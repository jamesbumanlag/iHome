# Generated by Django 5.0.6 on 2024-07-04 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_rename_person_progressnotes_persons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progressnotes',
            old_name='persons',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='progressnotes',
            old_name='progress_notes',
            new_name='progress_note',
        ),
        migrations.AlterField(
            model_name='progressnotes',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='progressnotes',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
    ]
