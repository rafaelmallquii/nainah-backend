# Generated by Django 4.2.1 on 2023-06-28 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
