from django.contrib.auth import validators
from django.db import models
from webcolors.constants import CSS3_NAMES_TO_HEX
from colorfield.fields import ColorField
from users.models import User
from constants import API_FIELD_LENGHT


class Ingredient(models.Model):
    """Модель ингредиентов."""

    name = models.CharField(
        max_length=API_FIELD_LENGHT, blank=False, verbose_name="Название ингредиента"
    )

    measurement_unit = models.CharField(
        max_length=API_FIELD_LENGHT, blank=False, verbose_name="Единицы измерения"
    )

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    """Модель Рецепта."""

    author = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Автор",
    )
    name = models.CharField(
        blank=False, max_length=API_FIELD_LENGHT, verbose_name="Название рецепта"
    )
    image = models.ImageField(blank=False, verbose_name="Картинка")
    text = models.TextField(blank=False, verbose_name="Описание")
    ingredients = models.ManyToManyField(
        blank=False,
        to="IngredientsInRecipe",
        related_name="recipes",
        verbose_name="Ингредиенты",
    )
    tags = models.ManyToManyField(blank=False, to="Tag", verbose_name="Теги")
    cooking_time = models.IntegerField(blank=False, verbose_name="Время приготовления")

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return self.name


class IngredientsInRecipe(models.Model):
    ingredient = models.ForeignKey(
        to=Ingredient, on_delete=models.CASCADE, verbose_name="Ингредиент"
    )
    amount = models.IntegerField(blank=False, verbose_name="Количество")

    def __str__(self) -> str:
        return self.ingredient.name


class Tag(models.Model):
    """Модель тега."""

    name = models.CharField(blank=False, max_length=API_FIELD_LENGHT, verbose_name="Название")
    color = ColorField(
        blank=False,
        verbose_name="Цвет",
        help_text="HEX цвета подставляеться автоматически",
    )
    slug = models.SlugField(
        blank=False,
        max_length=API_FIELD_LENGHT,
        unique=True,
        verbose_name="Slug тега",
        help_text="Должен быть уникальным",
    )

    def __str__(self) -> str:
        return self.name
