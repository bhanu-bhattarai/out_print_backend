# Generated by Django 3.0.2 on 2020-03-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_auto_20200316_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
