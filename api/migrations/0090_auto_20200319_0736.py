# Generated by Django 3.0.2 on 2020-03-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0089_auto_20200319_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(choices=[('cs', 'CS'), ('it', 'IT'), ('electronics', 'Electronics'), ('mechanical', 'Mechanical'), ('other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(choices=[('b-tech', 'B-Tech'), ('mca', 'MCA'), ('bca', 'BCA'), ('ba', 'BA'), ('bsc', 'BSc'), ('other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('other', 'Other')], max_length=50, null=True),
        ),
    ]
