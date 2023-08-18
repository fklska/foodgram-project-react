from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import response, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from users.models import Favorite, ShoppingCart
from users.serializers import ReceptLiteSerializer

from .filters import IngredientsFilter, RecipeFilter
from .models import Ingredient, IngredientsInRecipe, Recipe, Tag
from .premissions import AuthorizedOrAuthor
from .serializers import IngredientSerizlizer, ReceptSerizlizer, TagSerizlizer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = ReceptSerizlizer
    permission_classes = [AuthorizedOrAuthor]
    filter_backends = [RecipeFilter]

    @action(
        detail=True, methods=["post", "delete"], permission_classes=[IsAuthenticated]
    )
    def favorite(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        if request.method == "POST":
            favorite, is_create = Favorite.objects.get_or_create(
                recipe=recipe, user=request.user
            )

            if is_create:
                serializer = ReceptLiteSerializer(
                    favorite.recipe, context={"request": self.request}
                )
                return response.Response(data=serializer.data)

            return response.Response(
                "Alredy in favorite", status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == "DELETE":
            favorite = get_object_or_404(Favorite, user=request.user, recipe=recipe)
            favorite.delete()
            return response.Response("success", status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=True, methods=["post", "delete"], permission_classes=[IsAuthenticated]
    )
    def shopping_cart(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        if request.method == "POST":
            shoping, is_create = ShoppingCart.objects.get_or_create(
                user=request.user, recipe=recipe
            )

            if is_create:
                serializer = ReceptLiteSerializer(
                    shoping.recipe, context={"request": self.request}
                )
                return response.Response(data=serializer.data)

            return response.Response(
                "Already in shopping cart", status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == "DELETE":
            shoping = get_object_or_404(ShoppingCart, user=request.user, recipe=recipe)
            shoping.delete()
            return response.Response("success", status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["Get"], permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = IngredientsInRecipe.objects.filter(
            recipes__shopping__user=request.user
        ).all()
        # Ing --> Recept --> ShoppingCart --> User --> сравниваю пользователей
        #q = ingredients.annotate(Count('amount', distinct=True))
        #print(q[0].amount)
        print(ingredients)
        result = {}
        for ing in ingredients:
            result[f"{ing.ingredient.name}" f"({ing.ingredient.measurement_unit})"] = (
                result.get(
                    f"{ing.ingredient.name} ({ing.ingredient.measurement_unit})", 0
                )
                + ing.amount
            )
        print(result)
        #  Ключ - название ингредиента + ед. изм.
        #  Значение - количество
        with open("shopping_list.txt", "w", encoding="utf8") as file:
            for key in result.keys():
                file.write(f"{key} - {result[key]} \n")

        return FileResponse(open("shopping_list.txt", "rb"))


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerizlizer
    pagination_class = None
    http_method_names = ["get"]


class IngeredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerizlizer
    filter_backends = [IngredientsFilter]
    pagination_class = None
    search_fields = ["^name"]
