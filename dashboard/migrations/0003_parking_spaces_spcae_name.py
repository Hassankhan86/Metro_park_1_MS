# Generated by Django 3.2.5 on 2021-07-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_customer_vehicle_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking_spaces',
            name='spcae_name',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
