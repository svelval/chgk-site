# Generated by Django 5.0.8 on 2024-10-14 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0004_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
