# Generated by Django 3.0.2 on 2020-03-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20200309_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('requested', 'Requested'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('active', 'Active'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
