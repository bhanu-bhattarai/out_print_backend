# Generated by Django 3.0.2 on 2020-03-13 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_auto_20200313_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='get_freemium',
        ),
    ]
