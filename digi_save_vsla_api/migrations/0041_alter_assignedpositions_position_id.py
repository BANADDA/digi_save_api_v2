# Generated by Django 4.2.7 on 2023-11-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0040_alter_users_email_alter_users_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedpositions',
            name='position_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]