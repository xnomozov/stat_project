# Generated by Django 5.0.7 on 2024-07-25 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
            preserve_default=False,
        ),
    ]
