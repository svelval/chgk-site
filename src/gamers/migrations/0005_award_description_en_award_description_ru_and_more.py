# Generated by Django 5.0.8 on 2024-10-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0004_award_name_alter_award_codename'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='award',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='award',
            name='name_en',
            field=models.CharField(null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='award',
            name='name_ru',
            field=models.CharField(null=True, verbose_name='name'),
        ),
    ]
