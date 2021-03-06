# Generated by Django 3.0.2 on 2020-04-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0113_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('details_of_enquiry', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'contact_us',
            },
        ),
    ]
