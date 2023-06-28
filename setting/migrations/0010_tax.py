# Generated by Django 4.2.1 on 2023-06-20 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0009_remove_setting_site_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setting.setting')),
            ],
            options={
                'verbose_name_plural': 'Tax',
            },
        ),
    ]
