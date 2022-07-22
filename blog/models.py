from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    post_views = models.PositiveIntegerField(default=0)
    image_home = models.ImageField(upload_to='post/', blank=True, null=True)
    image_detail_body = models.ImageField(upload_to='post/', blank=True, null=True)
    created_at = models.DateField()
    description_one = models.TextField()
    description_two = models.TextField()
    category = models.ManyToManyField(Category, related_name='post_category')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

