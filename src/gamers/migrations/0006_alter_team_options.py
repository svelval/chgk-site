# Generated by Django 5.0.8 on 2024-10-14 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0005_award_description_en_award_description_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
    ]
