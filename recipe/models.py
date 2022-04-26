from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class RecipeIngredient(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

