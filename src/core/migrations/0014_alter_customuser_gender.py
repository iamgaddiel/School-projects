# Generated by Django 4.0.4 on 2022-05-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_driverslicense_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('male', 'male'), ('female', 'female')], default=('male', 'male'), max_length=6),
        ),
    ]
