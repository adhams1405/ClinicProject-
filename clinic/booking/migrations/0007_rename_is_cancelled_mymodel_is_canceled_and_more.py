# Generated by Django 5.0.6 on 2024-07-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_mymodel_delete_appointment_cancel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='is_cancelled',
            new_name='is_canceled',
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
