# Generated by Django 3.2 on 2024-01-01 16:55

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0012_alter_reservation_num_of_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_of_booking',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time_of_booking',
            field=models.IntegerField(choices=[(0, datetime.time(12, 30)), (1, datetime.time(13, 0)), (2, datetime.time(13, 30)), (3, datetime.time(14, 0)), (4, datetime.time(14, 30)), (5, datetime.time(20, 0)), (6, datetime.time(20, 30)), (7, datetime.time(21, 0)), (8, datetime.time(21, 30))], default=0),
        ),
    ]
