# Generated by Django 3.0.2 on 2020-06-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0125_auto_20200610_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sem',
            field=models.IntegerField(choices=[(1, 1), (2, 2)], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
    ]
