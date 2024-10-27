# Generated by Django 5.0.8 on 2024-10-26 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_group_group_index_alter_group_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['game_index'], 'verbose_name': 'Game', 'verbose_name_plural': 'Games'},
        ),
        migrations.RenameField(
            model_name='game',
            old_name='group_index',
            new_name='game_index',
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('group', 'game_index')},
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('season', 'group_index')},
        ),
    ]