# Generated by Django 5.0.4 on 2024-05-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_customuserpermissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='studios',
            name='del_stamp',
            field=models.DateTimeField(null=True),
        ),
    ]
