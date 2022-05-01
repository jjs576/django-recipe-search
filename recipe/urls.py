from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RecipeViewSet,
    IngredientViewSet,
)

app_name = 'recipe'

router = DefaultRouter()
router.register('recipe', RecipeViewSet)
router.register('ingredient', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
