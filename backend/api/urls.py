from django.urls import path, include
from rest_framework import routers
from .views import TagViewSet, RecipeViewSet, IngeredientViewSet

router = routers.DefaultRouter()
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)
router.register('ingredients', IngeredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]
