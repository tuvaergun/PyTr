from django.contrib import admin
from blog.models import Categories, Posts

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','author','description','created','edited')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(Categories, CategoriesAdmin)