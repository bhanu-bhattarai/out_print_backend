# Generated by Django 3.0.2 on 2020-06-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0129_auto_20200616_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincode',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]