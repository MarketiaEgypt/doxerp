from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Services(models.Model):
	image = models.ImageField(upload_to='icon-services/', blank=True, null=True)
	name = models.CharField(max_length=40)
	description = models.TextField(max_length=10000)
	slug = models.SlugField(blank=True, null=True)
	meta_title = models.CharField(max_length=200, blank=True)
	meta_description = models.TextField(max_length=500, blank=True)
	keywords = models.TextField(max_length=500, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Services, self).save(*args, **kwargs) # Call the real save() method

	def __str__(self):
		return self.name


class Solutions(models.Model):
	image = models.ImageField(upload_to='icon-solutions/', blank=True, null=True)
	name = models.CharField(max_length=40)
	description = models.TextField(max_length=10000)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Solutions, self).save(*args, **kwargs) # Call the real save() method

	def __str__(self):
		return self.name