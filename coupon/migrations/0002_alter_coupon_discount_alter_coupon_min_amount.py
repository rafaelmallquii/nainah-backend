# Generated by Django 4.2.1 on 2023-05-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(help_text='Discount in USD'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='min_amount',
            field=models.DecimalField(decimal_places=2, help_text='Minimum amount to apply coupon', max_digits=10),
        ),
    ]
