# Generated by Django 4.2.7 on 2023-11-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_alter_room_size_alter_schedule_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Talaba hujjati', 'verbose_name_plural': 'Talaba hujjatlari'},
        ),
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(default=' ', verbose_name='Fayl haqida'),
        ),
    ]