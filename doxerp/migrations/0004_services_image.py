# Generated by Django 4.0.4 on 2022-07-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doxerp', '0003_rename_image_services_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='icon-services/'),
        ),
    ]