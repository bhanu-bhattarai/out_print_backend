# Generated by Django 3.0.2 on 2020-04-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0112_auto_20200407_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'states',
            },
        ),
    ]
