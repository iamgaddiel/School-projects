# Generated by Django 4.0.4 on 2022-05-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('O+', '0+'), ('O-', '0-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B+')], default='', max_length=2),
        ),
    ]
