# Generated by Django 5.0.8 on 2024-10-02 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='BasePlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(verbose_name='first name')),
                ('last_name', models.CharField(verbose_name='last name')),
                ('about', models.TextField(verbose_name='description')),
                ('awards', models.ManyToManyField(to='gamers.award', verbose_name='awards')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Connoisseur',
            fields=[
                ('baseplayer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gamers.baseplayer')),
                ('won_games', models.PositiveIntegerField(default=0, verbose_name='won games')),
                ('total_games', models.PositiveIntegerField(default=0, verbose_name='total games')),
                ('first_game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.game', verbose_name='first game')),
            ],
            bases=('gamers.baseplayer',),
        ),
        migrations.CreateModel(
            name='TVViewer',
            fields=[
                ('baseplayer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gamers.baseplayer')),
            ],
            bases=('gamers.baseplayer',),
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('connoisseur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gamers.connoisseur')),
                ('is_capitan', models.BooleanField(default=False, verbose_name='is capitan')),
            ],
            bases=('gamers.connoisseur',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('won_games', models.PositiveIntegerField(default=0, verbose_name='won games')),
                ('total_games', models.PositiveIntegerField(default=0, verbose_name='total games')),
                ('first_game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.game', verbose_name='first game')),
                ('players', models.ManyToManyField(to='gamers.teamplayer', verbose_name='gamers')),
            ],
        ),
    ]