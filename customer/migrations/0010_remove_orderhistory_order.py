# Generated by Django 4.2.1 on 2023-06-22 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_remove_orderhistory_orders_orderhistory_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='order',
        ),
    ]