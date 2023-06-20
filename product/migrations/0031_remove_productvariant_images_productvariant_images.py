# Generated by Django 4.2.1 on 2023-06-14 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_productimage_remove_productvariant_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='images',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productimage'),
        ),
    ]
