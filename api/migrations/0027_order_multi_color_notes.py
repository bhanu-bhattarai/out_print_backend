# Generated by Django 3.0.2 on 2020-03-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200305_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='multi_color_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
