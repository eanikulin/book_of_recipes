from django.contrib import admin
from .models import Category, Recipe, RecipeCategory


class RecipeCategoryInline(admin.TabularInline):
    model = RecipeCategory


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'time_create', 'time_update')
    list_filter = ('is_published', 'categories')
    search_fields = ('title', 'author__username')
    inlines = [RecipeCategoryInline]


admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
