# Generated by Django 4.2.1 on 2023-06-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_order_shipping_charge_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
