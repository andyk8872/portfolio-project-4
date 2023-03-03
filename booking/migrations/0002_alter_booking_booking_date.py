# Generated by Django 3.2.18 on 2023-03-02 07:22

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(datetime.date(2023, 3, 12))], verbose_name='Booking date'),
        ),
    ]