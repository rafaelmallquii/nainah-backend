# Generated by Django 4.2.1 on 2023-06-20 00:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0042_remove_product_size_remove_productvariant_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default='\n<h2><img alt="" src="https://i.imgur.com/e6bpDkz.png" style="height:33px; width:42px" />\n<img alt="" src="https://imgur.com/a/LpSz4ZC" />&nbsp; Nainah Collection</h2>\n<hr />\n<p>&nbsp;</p>\n'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Nainah Collection', max_length=100),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
