from rest_framework.filters import BaseFilterBackend, SearchFilter


class IngredientsFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_favorite = request.query_params.get('is_favorite')
        author = request.query_params.get('author')
        is_in_shopping_cart = request.query_params.get('is_in_shopping_cart')
        tags = request.query_params.get('tags')
        if is_favorite is not None:
            queryset = queryset.filter(favorites__user=request.user)
        if author is not None:
            queryset = queryset.filter(author__username=author)
        if is_in_shopping_cart is not None:
            queryset = queryset.filter(shopping__user=request.user)
        if tags is not None:
            queryset = queryset.filter(tags__slug=tags)
        return queryset
