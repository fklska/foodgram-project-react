from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters


class IngredientsFilter(SearchFilter):
    search_param = "name"


class RecipeFilter(filters.FilterSet):
    is_favorited = filters.BooleanFilter(method='favorite_filter')
    is_in_shopping_cart = filters.BooleanFilter(method='shopping_cart_filter')
    tags = filters.CharFilter(method='tags_filter')
    author = filters.CharFilter(method='author_filter')

    def author_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author__username=value)
        return queryset

    def tags_filter(self, queryset, name, value):
        if value:
            return queryset.filter(tags__slug=value)
        return queryset

    def favorite_filter(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def shopping_cart_filter(self, queryset, name, value):
        if value:
            return queryset.filter(shopping__user=self.request.user)
        return queryset
