# Generated by Django 3.0.2 on 2020-03-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0104_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='front_cover_pdf_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(auto_created=True, choices=[('incomplete', 'Incomplete'), ('confirmed', 'Confirmed'), ('assigned', 'Assigned'), ('processing', 'Processing'), ('departed', 'Departed'), ('out-for-delivery', 'Out for Delivery'), ('delivered', 'Delivered')], default='confirmed', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
