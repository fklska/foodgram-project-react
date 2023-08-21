from django.contrib.auth import validators
from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import EMAIL_FIELD_LENGHT, USER_FIELD_LENGHT


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        blank=False,
        max_length=USER_FIELD_LENGHT,
        validators=(
            [validators.UnicodeUsernameValidator(regex=r"^[\w.@+-]+\Z")]
        ),
        unique=True,
    )
    password = models.CharField(
        blank=False,
        max_length=USER_FIELD_LENGHT,
    )
    first_name = models.CharField(
        blank=False,
        max_length=USER_FIELD_LENGHT,
    )
    last_name = models.CharField(
        blank=False,
        max_length=USER_FIELD_LENGHT,
    )
    email = models.EmailField(
        blank=False,
        max_length=EMAIL_FIELD_LENGHT,
    )

    def __str__(self) -> str:
        return self.username


class Follow(models.Model):
    subscriber = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="followings",
        verbose_name="Подписщик",
        help_text="Подписки относительно request.user",
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        help_text="Подписчики относительно request.user",
        related_name="followers",
    )


class Favorite(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    recipe = models.ForeignKey(
        to="api.Recipe", on_delete=models.CASCADE, related_name="favorites"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "recipe"), name="Already in favorite"
            )
        ]


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    recipe = models.ForeignKey(
        to="api.Recipe",
        on_delete=models.CASCADE,
        related_name="shopping",
        verbose_name="Рецепт",
    )
