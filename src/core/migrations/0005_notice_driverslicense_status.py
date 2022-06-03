# Generated by Django 4.0.4 on 2022-05-11 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_customuser_height_alter_customuser_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(default='notice_image.jpg', upload_to='notice_images')),
                ('location', models.TextField(help_text='The locality where project is needed')),
                ('tools', models.CharField(help_text='separate tools by using comma(,)', max_length=400)),
                ('description', models.TextField(blank=True)),
                ('Timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='driverslicense',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
