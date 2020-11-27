# Generated by Django 3.0.2 on 2020-03-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_remove_order_page_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='page_config',
            field=models.CharField(choices=[('one-sided', 'One-Sided'), ('two-sided', 'Two-Sided')], default='one-sided', max_length=20),
        ),
    ]
