from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter


class IngredientsFilter(SearchFilter):
    search_param = "name"


class RecipeFilter(filters.FilterSet):
    is_favorited = filters.BooleanFilter(method="get_favorite")
    is_in_shopping_cart = filters.BooleanFilter(method="get_shopping_cart")
    tags = filters.CharFilter(method="get_tags")
    author = filters.CharFilter(method="get_author")

    def get_author(self, queryset, name, value):
        if value:
            return queryset.filter(author__id=value)
        return queryset

    def get_tags(self, queryset, name, value):
        if value:
            return queryset.filter(tags__slug=value)
        return queryset

    def get_favorite(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def get_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(shopping__user=self.request.user)
        return queryset
