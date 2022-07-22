from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from blog.models import Category, Post, Tag


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
