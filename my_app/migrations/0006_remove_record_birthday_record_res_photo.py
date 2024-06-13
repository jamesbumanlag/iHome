# Generated by Django 5.0.6 on 2024-06-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_remove_record_res_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='birthday',
        ),
        migrations.AddField(
            model_name='record',
            name='res_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/my_app/static/res_photo/'),
        ),
    ]
