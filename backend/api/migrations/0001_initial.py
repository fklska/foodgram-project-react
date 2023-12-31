# Generated by Django 4.2.4 on 2023-08-26 11:37

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200, verbose_name="Название ингредиента"
                    ),
                ),
                (
                    "measurement_unit",
                    models.CharField(max_length=200, verbose_name="Единицы измерения"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IngredientsInRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="Количество")),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Название рецепта"),
                ),
                ("image", models.ImageField(upload_to="", verbose_name="Картинка")),
                ("text", models.TextField(verbose_name="Описание")),
                (
                    "cooking_time",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Время приготовления",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Название")),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        help_text="HEX цвета подставляеться автоматически",
                        image_field=None,
                        max_length=18,
                        samples=None,
                        verbose_name="Цвет",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Должен быть уникальным",
                        max_length=200,
                        unique=True,
                        verbose_name="Slug тега",
                    ),
                ),
            ],
        ),
    ]
