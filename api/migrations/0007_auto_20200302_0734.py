# Generated by Django 3.0.2 on 2020-03-02 07:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(blank=True, max_length=20, null=True)),
                ('landmark', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('home', 'Home'), ('work', 'Work'), ('others', 'Others')], max_length=20, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='bindingConfig',
            field=models.CharField(blank=True, choices=[('loose_papers', 'Loose Papers'), ('stapled_copy', 'Stapled Copy'), ('spiral_binding', 'Spiral Binding')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='printingConfig',
            field=models.CharField(blank=True, choices=[('black_and_white', 'Black and White'), ('colored', 'Colored')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to='api.Addresses'),
            preserve_default=False,
        ),
    ]