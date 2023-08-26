from django.contrib import admin

from .models import Ingredient, IngredientsInRecipe, Recipe, Tag


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "author",
        "image",
        "text",
        "cooking_time",
        "amount_in_favorite",
        "pub_date"
    )
    list_editable = ("pub_date", "name",)
    list_filter = (
        "name",
        "author",
        "tags",
    )
    readonly_fields = ("amount_in_favorite",)
    search_fields = ("name", "author", "tags")

    def amount_in_favorite(self, obj):
        return obj.favorites.all().count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "color", "slug")


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "measurement_unit")
    search_fields = (
        "name",
        "id",
    )


@admin.register(IngredientsInRecipe)
class IngredientsInRecipeAdmin(admin.ModelAdmin):
    list_display = ("ingredient", "id", "amount")
