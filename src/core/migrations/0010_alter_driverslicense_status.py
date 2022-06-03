# Generated by Django 4.0.4 on 2022-05-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_driverslicense_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverslicense',
            name='status',
            field=models.CharField(choices=[('approved', 'approved'), ('declined', 'declined'), ('expired', 'expired'), ('pending', 'pending')], default='pending', max_length=10),
        ),
    ]
