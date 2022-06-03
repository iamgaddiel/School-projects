# Generated by Django 4.0.4 on 2022-05-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customuser_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='home_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(blank=True),
        ),
    ]
