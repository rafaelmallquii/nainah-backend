# Generated by Django 4.2.1 on 2023-06-30 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0025_rename_tax_taxandshipment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxandshipment',
            options={'verbose_name_plural': 'Tax and Shipment'},
        ),
        migrations.AddField(
            model_name='taxandshipment',
            name='shipment_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Enter shipment amount.', max_digits=10),
        ),
    ]
