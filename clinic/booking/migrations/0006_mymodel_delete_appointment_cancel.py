# Generated by Django 5.0.6 on 2024-07-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_appointment_cancel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_cancelled', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment_Cancel',
        ),
    ]
