# Generated by Django 4.2.5 on 2023-09-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0006_remove_customer_data_id_customer_data_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_data',
            name='ID',
        ),
        migrations.AddField(
            model_name='customer_data',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
