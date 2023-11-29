# Generated by Django 4.2.7 on 2023-11-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tel raqam'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telegram full name'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='tg_id',
            field=models.IntegerField(unique=True, verbose_name='Telegram id'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(blank=True, db_index=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=50, null=True, unique=True, verbose_name='Telegram username'),
        ),
    ]
