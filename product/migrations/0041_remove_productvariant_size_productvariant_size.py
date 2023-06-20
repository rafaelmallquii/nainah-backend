# Generated by Django 4.2.1 on 2023-06-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_size_remove_product_size_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='size',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.ManyToManyField(blank=True, to='product.size'),
        ),
    ]
