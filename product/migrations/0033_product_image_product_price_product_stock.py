# Generated by Django 4.2.1 on 2023-06-14 00:22

from django.db import migrations, models
import product.utils


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_remove_productvariant_images_productvariant_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[product.utils.validator_price]),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
