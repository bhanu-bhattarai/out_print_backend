# Generated by Django 3.0.2 on 2020-03-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0096_auto_20200319_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]