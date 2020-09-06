# Generated by Django 2.2.6 on 2020-08-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200809_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(related_name='readers', through='p_library.Reading', to='p_library.Friend', verbose_name='Читатели'),
        ),
    ]
