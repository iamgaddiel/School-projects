# Generated by Django 3.1.6 on 2022-06-07 23:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_group_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='group name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(blank=True, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
