# Generated by Django 4.0.2 on 2022-05-11 06:16

import cafe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0017_alter_reserve_email_alter_reserve_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='image',
            field=models.ImageField(default='', upload_to=cafe.models.worker_image_upload),
        ),
    ]
