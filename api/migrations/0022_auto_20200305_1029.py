# Generated by Django 3.0.2 on 2020-03-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200305_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresses',
            name='point',
        ),
        migrations.AddField(
            model_name='addresses',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True),
        ),
    ]
