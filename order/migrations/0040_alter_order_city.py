# Generated by Django 4.2.1 on 2023-06-30 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0026_alter_taxandshipment_options_and_more'),
        ('order', '0039_alter_order_shipping_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.ForeignKey(help_text='Select City.', on_delete=django.db.models.deletion.CASCADE, to='setting.taxandshipment'),
        ),
    ]
