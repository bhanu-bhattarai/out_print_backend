# Generated by Django 3.0.2 on 2020-03-05 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200302_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
