# Generated by Django 4.2.1 on 2023-06-20 09:58

from django.db import migrations, models
import product.utils


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0044_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offert_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[product.utils.validator_price]),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='stock',
            field=models.PositiveBigIntegerField(default=0, help_text='Stock of this variant'),
        ),
    ]
