# Generated by Django 3.0.2 on 2020-03-25 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0107_pincode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]
