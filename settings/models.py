import os
from uuid import uuid4

from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Setting(models.Model):
    site_name = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(upload_to='settings_logo/', blank=True)
    favicon = models.ImageField(upload_to='settings_favicon/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    description = models.TextField(max_length=10000, blank=True)
    description_footer = models.TextField(max_length=10000, blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    linkedin_link = models.URLField(max_length=200, blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(max_length=500, blank=True)
    keywords = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        super().save()
        if self.logo:
            image = Image.open(self.logo.path)

            if self.logo.size > 2 * 1024 * 1024:
                raise ValidationError('Image Size More Than 2MB')

            elif self.logo.size >= 301 * 1024 and self.logo.size <= 700 * 1024:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.logo.path, quality=100)

            elif self.logo.size >= 31 * 1024 and self.logo.size <= 300 * 1024:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.logo.path, quality=100)


            elif self.logo.size >= 20 * 1024 and self.logo.size <= 30 *1024:
                return image

            elif self.logo.size <= 10 * 1024:
                return image
                # raise ValidationError('Image Size More Than 30 kB')

            else:
                raise ValidationError('Not Resized Image')

        if self.favicon:
            imageicon = Image.open(self.favicon.path)

            if self.favicon.size > 2 * 1024 * 1024:
                raise ValidationError('Image Size More Than 2MB')

            elif self.favicon.size >= 301 * 1024 and self.favicon.size <= 700 * 1024:
                w = int((imageicon.width) / 4)
                h = int((imageicon.height) / 4)
                resized = imageicon.resize((w, h))
                resized.save(self.favicon.path, quality=100)

            elif self.favicon.size >= 31 * 1024 and self.favicon.size <= 300 * 1024:
                w = int((imageicon.width) / 3)
                h = int((imageicon.height) / 3)
                resized = imageicon.resize((w, h))
                resized.save(self.favicon.path, quality=100)

            elif self.favicon.size <= 10 * 1024:
                return image
                #raise ValidationError('Image Size More Than 30 kB')

            else:
                raise ValidationError('Not Resized Image')


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    massege = models.TextField(max_length=10000)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


def path_and_rename(instance, filename):
    upload_to = 'clients_logo'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class ClientLogo(models.Model):
    image = models.ImageField(upload_to=path_and_rename, blank=True)
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ClientLogo, self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image.path)

            if self.image.size > 2 * 1024 * 1024:
                raise ValidationError('Image Size More Than 2MB')

            elif self.image.size >= 301 * 1024 and self.image.size <= 700 * 1024:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.image.path, quality=100)

            elif self.image.size >= 150 * 1024 and self.logo.size <= 300 * 1024:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.image.path, quality=100)

            elif self.image.size >= 30 * 1024 and self.image.size <= 50 *1024:
                return image

            elif self.image.size <= 20 * 1024:
                return image
                # raise ValidationError('Image Size More Than 30 kB')

            else:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.image.path, quality=100)

    def __str__(self):
        return self.title



