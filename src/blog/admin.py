from django.contrib import admin
from blog.models import Categories, Posts
from django import forms
from django.db import models

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','author','description','created','edited')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    class Media:
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Posts, PostsAdmin)
admin.site.register(Categories, CategoriesAdmin)