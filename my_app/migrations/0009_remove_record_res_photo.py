# Generated by Django 5.0.6 on 2024-06-13 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_record_res_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='res_photo',
        ),
    ]