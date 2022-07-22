# Generated by Django 4.0.4 on 2022-05-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_ar', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ar', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('author_ar', models.CharField(max_length=100, null=True)),
                ('author_en', models.CharField(max_length=100, null=True)),
                ('image_author', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('title', models.CharField(max_length=100)),
                ('title_ar', models.CharField(max_length=100, null=True)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('post_views', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('created_at', models.DateField()),
                ('description_one', models.TextField()),
                ('description_one_ar', models.TextField(null=True)),
                ('description_one_en', models.TextField(null=True)),
                ('description_two', models.TextField()),
                ('description_two_ar', models.TextField(null=True)),
                ('description_two_en', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ManyToManyField(related_name='post_category', to='blog.category')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]