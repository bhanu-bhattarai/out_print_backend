# Generated by Django 3.0.2 on 2020-03-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0103_auto_20200323_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(blank=True, choices=[('home', 'Home'), ('work', 'Work'), ('others', 'Others')], max_length=255, null=True),
        ),
    ]