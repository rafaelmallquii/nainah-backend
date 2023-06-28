# Generated by Django 4.2.1 on 2023-06-25 19:19

from django.db import migrations, models
import product.utils


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0054_alter_product_tags_alter_productvariant_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[product.utils.validator_price]),
        ),
    ]
