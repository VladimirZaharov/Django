# Generated by Django 3.2.9 on 2021-11-17 13:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211115_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 13, 2, 24, 218989, tzinfo=utc)),
        ),
    ]
