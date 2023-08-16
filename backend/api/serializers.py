import base64

import webcolors
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Favorite, ShoppingCart
from users.serializers import UserSerializer

from .models import Ingredient, IngredientsInRecipe, Recipe, Tag


class HexColor(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.name_to_hex(name=data)
        except ValueError:
            raise serializers.ValidationError("No such color")
        return data


class IngredientSerizlizer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit', 'id')


class IngredientInRecipeRelationField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.ingredient.name,
            'measurement_unit': value.ingredient.measurement_unit,
            'amount': value.amount
        }

    def to_internal_value(self, data):
        obj, _ = IngredientsInRecipe.objects.get_or_create(
            amount=data.get('amount'),
            ingredient=get_object_or_404(Ingredient, id=data.get('id'))
        )
        return obj


class TagSerizlizer(serializers.ModelSerializer):
    slug = serializers.CharField(
        max_length=200,
        required=True,
        validators=[UniqueValidator(
            queryset=Tag.objects.all(),
            message="This slug already exist")
        ]
    )

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class TagRelationField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.name,
            'color': value.color,
            'slug': value.slug
            }

    def to_internal_value(self, data):
        return data


class ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext,)
        return super().to_internal_value(data)


class ReceptSerizlizer(serializers.ModelSerializer):
    ingredients = IngredientInRecipeRelationField(
        queryset=IngredientsInRecipe.objects.all(),
        many=True
    )
    tags = TagRelationField(many=True, queryset=Tag.objects.all())
    author = UserSerializer(required=False)
    image = ImageField(required=False)
    is_favorited = serializers.SerializerMethodField(
        method_name='get_favorite'
    )
    is_in_shopping_cart = serializers.SerializerMethodField(
        method_name='get_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author',
            'ingredients', 'is_favorited', 'is_in_shopping_cart',
            'name', 'image', 'text', 'cooking_time',
        )

    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recept = Recipe.objects.create(**validated_data)
        recept.tags.set(tags)
        recept.ingredients.set(ingredients)
        return recept

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        ingeredients = validated_data.pop('ingredients')
        Recipe.objects.filter(id=instance.id).update(**validated_data)
        recept = Recipe.objects.filter(id=instance.id).get()

        recept.tags.set(tags)
        recept.ingredients.set(ingeredients)
        return recept

    def get_favorite(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            if Favorite.objects.filter(user=user, recipe=obj).exists():
                return True
        return False

    def get_shopping_cart(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            if ShoppingCart.objects.filter(user=user, recipe=obj).exists():
                return True
        return False
