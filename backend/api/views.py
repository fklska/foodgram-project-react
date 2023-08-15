from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, response, status
from .models import Recept, Tag, Ingredient, IngredientsInRecipe
from .serializers import ReceptSerizlizer, TagSerizlizer, IngredientSerizlizer
from users.serializers import UserSerializer
from rest_framework.decorators import action
from users.models import Favorite, ShoppingCart
from users.serializers import ReceptLiteSerializer
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from .premissions import AuthorizedOrAuthor
from rest_framework import filters
from .filters import RecipeFilter, IngredientsFilter


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recept.objects.all()
    serializer_class = ReceptSerizlizer
    permission_classes = [AuthorizedOrAuthor]
    filter_backends = [RecipeFilter]

    @action(detail=True, methods=['post', 'delete'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        recipe = get_object_or_404(Recept, id=pk)
        if request.method == 'POST':
            favorite, is_create = Favorite.objects.get_or_create(recipe=recipe, user=request.user)
            if is_create:
                serializer = ReceptLiteSerializer(favorite.recipe, context={'request': self.request})
                return response.Response(data=serializer.data)
            return response.Response("Alredy in favorite", status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            favorite = get_object_or_404(Favorite, user=request.user, recipe=recipe)
            favorite.delete()
            return response.Response("succes", status=status.HTTP_204_NO_CONTENT)

        return None

    @action(detail=True, methods=['post', 'delete'], permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk):
        recipe = get_object_or_404(Recept, id=pk)
        if request.method == 'POST':
            shoping, is_create = ShoppingCart.objects.get_or_create(user=request.user, recipe=recipe)
            if is_create:
                serializer = ReceptLiteSerializer(shoping.recipe, context={'request': self.request})
                return response.Response(data=serializer.data)
            return response.Response("Already in shopping cart", status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            shoping = get_object_or_404(ShoppingCart, user=request.user, recipe=recipe)
            shoping.delete()
            return response.Response("succes", status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['Get'], permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = IngredientsInRecipe.objects.filter(recepts__shopping__user=request.user).all() #Через related name обращаюсь к модели Recept --> через related name (shopping) модели Recept обращаюсь к модели ShoppingCart, в этой модели есть поле user --> сравниваю пользователей
        result = {}
        for ing in ingredients:
            result[f'{ing.ingredient.name} ({ing.ingredient.measurement_unit})'] = result.get(f'{ing.ingredient.name} ({ing.ingredient.measurement_unit})', 0) + ing.amount
        with open('shopping_list.txt', 'w', encoding='utf8') as file:
            for key in result.keys():
                file.write(f'{key} - {result[key]} \n')
        return FileResponse(open('shopping_list.txt', 'rb'))


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerizlizer
    pagination_class = None
    http_method_names = ['get']


class IngeredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerizlizer
    filter_backends = [IngredientsFilter]
    pagination_class = None
    search_fields = ['^name']
