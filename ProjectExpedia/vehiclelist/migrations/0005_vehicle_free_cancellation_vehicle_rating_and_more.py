# Generated by Django 5.1.2 on 2024-11-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclelist', '0004_vehicle_imagefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='free_cancellation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='unlimited_milage',
            field=models.BooleanField(default=True),
        ),
    ]