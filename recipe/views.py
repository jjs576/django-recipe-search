from rest_framework.viewsets import ModelViewSet
from .models import Recipe, Ingredient
from .serializers import (
    IngredientSerializer, RecipeSerializer
)


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.alive_objects.all()
    serializer_class = RecipeSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.alive_objects.all()
    serializer_class = IngredientSerializer
