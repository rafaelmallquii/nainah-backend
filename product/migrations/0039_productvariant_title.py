# Generated by Django 4.2.1 on 2023-06-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0038_productvariant_stock_alter_productvariant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='title',
            field=models.CharField(default='Product Title', max_length=100),
        ),
    ]