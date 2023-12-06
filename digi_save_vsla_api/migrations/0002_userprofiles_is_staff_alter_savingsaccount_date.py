# Generated by Django 5.0 on 2023-12-05 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='savingsaccount',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2023, 12, 4)),
        ),
    ]
