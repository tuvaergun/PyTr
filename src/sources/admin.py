from django.contrib import admin
from sources.models import Categories, Sources, Types
from django import forms
from django.db import models

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}

class TypesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}

class SourcesAdmin(admin.ModelAdmin):
    list_display = ('title','author','description','created','edited')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Sources, SourcesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Types, TypesAdmin)