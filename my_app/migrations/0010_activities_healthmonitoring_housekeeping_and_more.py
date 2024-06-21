# Generated by Django 5.0.6 on 2024-06-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_remove_record_res_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companionship', models.CharField(max_length=100)),
                ('daily_activities', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HealthMonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgl', models.CharField(max_length=100)),
                ('bp', models.CharField(max_length=100)),
                ('o2', models.CharField(max_length=100)),
                ('pulse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Housekeeping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom', models.CharField(max_length=100)),
                ('laundry', models.CharField(max_length=100)),
                ('bedroom', models.CharField(max_length=100)),
                ('kitchen', models.CharField(max_length=100)),
                ('living', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MobilityAssistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer', models.CharField(max_length=100)),
                ('walking', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionHydration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeding_assistance', models.CharField(max_length=100)),
                ('food_intake', models.CharField(max_length=100)),
                ('fluid_intake', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathing', models.CharField(max_length=100)),
                ('dressing', models.CharField(max_length=100)),
                ('toileting', models.CharField(max_length=100)),
            ],
        ),
    ]