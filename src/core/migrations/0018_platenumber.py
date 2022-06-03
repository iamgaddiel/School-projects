# Generated by Django 4.0.4 on 2022-05-13 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rename__class_driverslicense_assigned_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlateNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivers_license', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(default='passports.jpg', upload_to='plate_number_owners_passowrds.jpg')),
                ('id_card', models.ImageField(default='id_card_image.jpg', upload_to='id_cards')),
                ('custom_papers', models.ImageField(blank=True, upload_to='')),
                ('delivery_note', models.ImageField(blank=True, upload_to='')),
                ('proof_of_ownership', models.ImageField(blank=True, upload_to='')),
                ('tax_id', models.CharField(max_length=20, unique=True)),
                ('insurance_papers', models.ImageField(blank=True, upload_to='')),
                ('engine_number', models.CharField(max_length=30, unique=True)),
                ('proof_of_address', models.ImageField(help_text='e.g. Utility Bill', upload_to='')),
                ('insurance_policy_number', models.CharField(max_length=20, unique=True)),
                ('issues_date', models.DateField(verbose_name='1900-01-01')),
                ('expiry_date', models.DateField(default='1900-01-01')),
                ('status', models.CharField(choices=[('approved', 'approved'), ('declined', 'declined'), ('expired', 'expired'), ('pending', 'pending')], max_length=10)),
                ('model_of_car', models.CharField(blank=True, max_length=30)),
                ('color', models.CharField(max_length=40)),
                ('plate_number', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
