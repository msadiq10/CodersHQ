# Generated by Django 3.2.11 on 2022-10-08 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20221008_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='linkedin',
            field=models.CharField(blank=True, help_text='https://linkedin.com/in/XXXX', max_length=100, null=True, validators=[django.core.validators.URLValidator], verbose_name='Linkedin account'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='twitter',
            field=models.CharField(blank=True, help_text='https://twitter.com/coders_hq', max_length=100, null=True, validators=[django.core.validators.URLValidator], verbose_name='Twitter account'),
        ),
    ]
