# Generated by Django 5.0 on 2024-09-07 16:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutDepartmentPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='dekanat/')),
                ('department', models.CharField(choices=[('dekanat', 'Dekanat'), ('kafedra', 'Kafedra'), ('tutor', 'Tyutor')], max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('reception_time', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('place', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='AboutFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('image1', models.ImageField(upload_to='about/')),
                ('image2', models.ImageField(upload_to='about/')),
                ('image3', models.ImageField(upload_to='about/')),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='news/')),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students/')),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
