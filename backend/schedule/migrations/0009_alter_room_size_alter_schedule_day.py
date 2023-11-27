# Generated by Django 4.2.7 on 2023-11-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_rename_number_room_room_schedule_lesson_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='size',
            field=models.IntegerField(default=30, verbose_name="Xona o'lchami"),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('Dushanba', 'Dushanba'), ('Seshanba', 'Seshanba'), ('Chorshanba', 'Chorshanba'), ('Payshanba', 'Payshanba'), ('Juma', 'Juma'), ('Shanba', 'Shanba')], default='Dushanba', max_length=50, verbose_name='Kun'),
        ),
    ]
