# Generated by Django 5.0.8 on 2024-10-07 17:26

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_alter_game_unique_together_game_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('year', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(2014), django.core.validators.MaxValueValidator(2024)], verbose_name='year')),
                ('rules', models.TextField(verbose_name='rules')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.season'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('season', 'group', 'group_index')},
        ),
        migrations.RemoveField(
            model_name='game',
            name='year',
        ),
    ]
