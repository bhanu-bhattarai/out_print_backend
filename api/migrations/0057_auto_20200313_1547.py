# Generated by Django 3.0.2 on 2020-03-13 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_user_is_freemium'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_freemium',
            new_name='get_freemium',
        ),
    ]