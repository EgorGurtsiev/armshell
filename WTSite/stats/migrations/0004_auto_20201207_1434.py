# Generated by Django 3.1.1 on 2020-12-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_tanks_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanks',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
