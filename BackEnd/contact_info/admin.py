from django.contrib import admin

from .models import City, Number


# Register your models here.

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title",)
    list_display_links = ("title",)


admin.site.register(City, CityAdmin)
admin.site.register(Number)
