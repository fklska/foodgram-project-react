from django.urls import include, path
from rest_framework import routers

from .views import IngeredientViewSet, RecipeViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)
router.register('ingredients', IngeredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]
