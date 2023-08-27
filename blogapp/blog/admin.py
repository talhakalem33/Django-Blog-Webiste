from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "isactive")

admin.site.register(Blog, BlogAdmin)
