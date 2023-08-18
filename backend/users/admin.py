from django.contrib import admin

from .models import Favorite, Follow, ShoppingCart, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "id", "email", "first_name", "last_name")
    list_filter = ("email", "username", "id")
    list_editable = ("email", "first_name", "last_name")
    search_fields = ("username", "email")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        "subscriber",
        "author",
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )
