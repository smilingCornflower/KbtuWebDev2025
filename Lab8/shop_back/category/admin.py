from django.contrib import admin

from category.models import Category


@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    pass
