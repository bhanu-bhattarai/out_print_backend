# Generated by Django 3.0.2 on 2020-03-19 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0075_auto_20200316_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_orders', to='api.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]