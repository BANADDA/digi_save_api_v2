# Generated by Django 4.2.7 on 2023-11-12 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0027_constitutiontable_constitution_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedpositions',
            name='position_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.positions'),
        ),
    ]
