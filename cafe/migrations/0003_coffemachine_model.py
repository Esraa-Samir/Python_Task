# Generated by Django 3.0.5 on 2020-09-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_coffepods'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffemachine',
            name='model',
            field=models.CharField(default='', max_length=200),
        ),
    ]
