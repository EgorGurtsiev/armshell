# Generated by Django 4.0.5 on 2022-07-01 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_player_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='account_id',
            new_name='id',
        ),
    ]
