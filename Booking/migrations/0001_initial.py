# Generated by Django 5.0.4 on 2024-05-01 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)])),
                ('type', models.CharField(max_length=20)),
                ('add_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]