# Generated by Django 4.0.4 on 2022-07-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_remove_clientlogo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientlogo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]