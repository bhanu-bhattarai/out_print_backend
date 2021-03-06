# Generated by Django 3.0.2 on 2020-03-21 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0098_order_delivery_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('assigned', 'Assigned'), ('processing', 'Processing'), ('out-for-delivery', 'Out for Delivery'), ('delivered', 'Delivered')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order_status',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='assigned_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivered_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='departed_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='processing_at',
        ),
        migrations.DeleteModel(
            name='AssignedOrder',
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_statuses', to='api.Order'),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
