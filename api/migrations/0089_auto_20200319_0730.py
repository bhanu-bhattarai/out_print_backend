# Generated by Django 3.0.2 on 2020-03-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0088_auto_20200319_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
