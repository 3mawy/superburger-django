# Generated by Django 3.1.7 on 2021-05-15 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210515_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_number',
            new_name='mobile_number',
        ),
    ]
