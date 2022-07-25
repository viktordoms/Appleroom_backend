from django.contrib import admin

from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title",)
    list_display_links = ("title",)

admin.site.register(Category, CategoryAdmin)
