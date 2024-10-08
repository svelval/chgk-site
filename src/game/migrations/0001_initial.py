# Generated by Django 5.0.8 on 2024-10-02 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False, verbose_name='date')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2014), django.core.validators.MaxValueValidator(2024)], verbose_name='year')),
                ('group', models.CharField(choices=[('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autumn'), ('winter', 'winter')], verbose_name='group')),
                ('group_index', models.PositiveIntegerField(verbose_name='game index')),
            ],
        ),
    ]
