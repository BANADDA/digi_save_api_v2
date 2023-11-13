# Generated by Django 4.2.7 on 2023-11-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0036_alter_activecyclemeeting_cyclemeetingid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cyclestartmeeting',
            name='group',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='member_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='group_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]