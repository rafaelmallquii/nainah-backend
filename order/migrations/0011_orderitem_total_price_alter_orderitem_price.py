# Generated by Django 4.2.1 on 2023-06-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_rename_price_sell_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
