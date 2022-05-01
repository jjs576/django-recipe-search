from django.db import models
from common.models import BaseModel


class Ingredient(BaseModel):
    name = models.CharField(max_length=255, null=False)
    kcal = models.IntegerField(default=0)


class Recipe(BaseModel):
    name = models.CharField(max_length=255, null=False)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    kcal = models.IntegerField(default=0)

    def calc_kcal(self):
        for i in self.ingredients.all():
            self.kcal += i.kcal
        self.save()


class RecipeProxy(Recipe):

    class Meta:
        proxy = True


class RecipeIngredient(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

