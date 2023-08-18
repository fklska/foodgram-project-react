from rest_framework import serializers

from api.models import Recipe

from .models import Follow, User


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField(method_name="get_subscribed")

    class Meta:
        model = User
        fields = ("email", "id", "username", "first_name", "last_name", "is_subscribed")

    def get_subscribed(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated and Follow.objects.filter(subscriber=user, author=obj).exists():
            return True
        return False


class ReceptLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id", "name", "image", "cooking_time")


class UserWithReceptSerializer(UserSerializer):
    recipes = serializers.SerializerMethodField(method_name="get_recipe")
    recipes_count = serializers.SerializerMethodField(method_name="get_count")

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_subscribed",
            "recipes",
            "recipes_count",
        )

    def get_recipe(self, obj):
        serializer = ReceptLiteSerializer(obj.recipes.all(), many=True)
        return serializer.data

    def get_count(self, obj):
        return Recipe.objects.filter(author=obj).count()
