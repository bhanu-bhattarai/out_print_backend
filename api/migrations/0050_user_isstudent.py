# Generated by Django 3.0.2 on 2020-03-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isStudent',
            field=models.BooleanField(default=True),
        ),
    ]