# Generated by Django 3.0.2 on 2020-03-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_auto_20200316_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
