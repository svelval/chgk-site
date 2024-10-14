# Generated by Django 5.0.8 on 2024-10-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_alter_season_options_alter_game_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='codename',
            field=models.CharField(verbose_name='codename'),
        ),
        migrations.AddField(
            model_name='group',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name_en',
            field=models.CharField(null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name_ru',
            field=models.CharField(null=True, verbose_name='name'),
        ),
    ]
