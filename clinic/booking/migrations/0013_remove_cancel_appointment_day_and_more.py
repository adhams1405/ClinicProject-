# Generated by Django 5.0.6 on 2024-07-11 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_remove_cancel_appointment_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancel_appointment',
            name='day',
        ),
        migrations.RemoveField(
            model_name='cancel_appointment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='cancel_appointment',
            name='user',
        ),
    ]
