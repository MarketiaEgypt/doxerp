# Generated by Django 4.0.4 on 2022-07-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_setting_address_ar_setting_address_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='settings_favicon/'),
        ),
    ]
