# Generated by Django 4.0.2 on 2022-05-04 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_alter_order_otime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='otime',
            field=models.TimeField(blank=True, default=datetime.time(9, 30, 8, 596628)),
        ),
    ]
