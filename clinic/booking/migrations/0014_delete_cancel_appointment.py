# Generated by Django 5.0.6 on 2024-07-11 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_remove_cancel_appointment_day_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cancel_appointment',
        ),
    ]
