# Generated by Django 4.2.1 on 2023-06-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_remove_orderhistory_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='extra_variable',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
