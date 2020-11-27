# Generated by Django 3.0.2 on 2020-06-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0118_auto_20200520_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='strike_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
