# Generated by Django 5.0.2 on 2024-02-24 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_zodiac_start_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zodiac',
            name='start_date_time',
        ),
    ]
