# Generated by Django 3.0.2 on 2020-03-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_auto_20200317_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='page_config',
            field=models.CharField(choices=[('one-sided', 'One-Sided'), ('two-sided', 'Two-Sided')], default='one_sided', max_length=20),
        ),
    ]
