# Generated by Django 4.2.1 on 2023-07-11 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_rename_contenido_newsletter_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='subject',
            field=models.CharField(default='Nainah Offerts', max_length=255),
            preserve_default=False,
        ),
    ]
