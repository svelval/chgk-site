# Generated by Django 5.0.8 on 2024-10-14 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_alter_game_unique_together_game_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.season', verbose_name='season'),
        ),
    ]
