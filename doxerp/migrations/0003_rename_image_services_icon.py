# Generated by Django 4.0.4 on 2022-07-17 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doxerp', '0002_alter_services_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='image',
            new_name='icon',
        ),
    ]