# Generated by Django 5.0.8 on 2024-10-03 19:51

import auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='no_photo.jpg', upload_to=auth.models.user_pic_path, verbose_name='avatar'),
        ),
    ]
