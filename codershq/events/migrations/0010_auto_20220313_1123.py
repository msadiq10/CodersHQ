# Generated by Django 3.2.11 on 2022-03-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20220313_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='event',
            name='requirements',
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(verbose_name='Event start date'),
        ),
    ]
