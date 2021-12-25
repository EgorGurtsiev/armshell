# Generated by Django 3.1.1 on 2020-12-15 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='название')),
                ('description', models.CharField(max_length=300, verbose_name='описание')),
                ('power', models.IntegerField(blank=True, verbose_name='сила')),
                ('commander', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='CompanyCommander', to=settings.AUTH_USER_MODEL, verbose_name='командир')),
            ],
            options={
                'verbose_name': 'Рота',
                'verbose_name_plural': 'Роты',
                'ordering': ['power'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
                ('executor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Контракт',
                'verbose_name_plural': 'Контракты',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='current_contract',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.contract'),
        ),
        migrations.AddField(
            model_name='company',
            name='field_commander',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='CompanyFieldCommander', to=settings.AUTH_USER_MODEL, verbose_name='полевой командир'),
        ),
    ]