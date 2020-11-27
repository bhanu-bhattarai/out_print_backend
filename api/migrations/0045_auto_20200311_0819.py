# Generated by Django 3.0.2 on 2020-03-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20200311_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(auto_created=True, choices=[('requested', 'Requested'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('active', 'Active'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='active', max_length=20),
        ),
    ]
