# Generated by Django 4.2.1 on 2023-06-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]