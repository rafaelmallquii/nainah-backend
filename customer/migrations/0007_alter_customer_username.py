# Generated by Django 4.2.1 on 2023-05-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
