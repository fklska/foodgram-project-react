from django.contrib import admin
from .models import Follow, Favorite, ShoppingCart, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', 'first_name', 'last_name')
    list_filter = ('email', 'username', 'id')
    list_editable = ('email', 'first_name', 'last_name')
    search_fields = ('username', 'email')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass
