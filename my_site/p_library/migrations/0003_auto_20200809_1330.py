# Generated by Django 2.2.6 on 2020-08-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200809_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='books',
            field=models.ManyToManyField(related_name='books', through='p_library.Reading', to='p_library.Book', verbose_name='Читает'),
        ),
    ]
