# Generated by Django 2.1.7 on 2020-05-12 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200512_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 12, 12, 34, 27, 771804)),
        ),
    ]
