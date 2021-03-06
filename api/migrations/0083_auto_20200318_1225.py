# Generated by Django 3.0.2 on 2020-03-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_auto_20200318_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='house_no',
            new_name='address_line2',
        ),
        migrations.RemoveField(
            model_name='address',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='address',
            name='lng',
        ),
        migrations.AddField(
            model_name='address',
            name='address_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(auto_created=True, choices=[('incomplete', 'Incomplete'), ('requested', 'Requested'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('active', 'Active'), ('cancelled', 'Cancelled'), ('departed', 'Departed'), ('completed', 'Completed')], default='accepted', max_length=20),
        ),
    ]
