# Generated by Django 4.2.7 on 2024-02-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aboutdepartmentpeople_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
