# Generated by Django 3.0.2 on 2020-03-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20200312_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=20, null=True),
        ),
    ]
