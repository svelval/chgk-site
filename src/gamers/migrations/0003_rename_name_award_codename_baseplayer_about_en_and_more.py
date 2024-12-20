# Generated by Django 5.0.8 on 2024-10-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0002_alter_award_options_alter_connoisseur_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='name',
            new_name='codename',
        ),
        migrations.AddField(
            model_name='baseplayer',
            name='about_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='baseplayer',
            name='about_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='baseplayer',
            name='first_name_en',
            field=models.CharField(null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='baseplayer',
            name='first_name_ru',
            field=models.CharField(null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='baseplayer',
            name='last_name_en',
            field=models.CharField(null=True, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='baseplayer',
            name='last_name_ru',
            field=models.CharField(null=True, verbose_name='last name'),
        ),
    ]
