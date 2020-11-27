# Generated by Django 3.0.2 on 2020-03-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_order_front_cover_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('print', 'Print'), ('binding', 'Binding'), ('others', 'Others')], max_length=20)),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'configurations',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='binding_config',
        ),
        migrations.RemoveField(
            model_name='order',
            name='printing_config',
        ),
        migrations.AddField(
            model_name='order',
            name='configurations',
            field=models.ManyToManyField(related_name='orders', to='api.Configuration'),
        ),
    ]