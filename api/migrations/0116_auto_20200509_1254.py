# Generated by Django 3.0.2 on 2020-05-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0115_connectwithus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='user',
            name='college_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]