# Generated by Django 4.2.7 on 2023-11-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('digi_save_vsla_api', '0002_alter_users_groups_alter_users_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups_test', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions_test', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
