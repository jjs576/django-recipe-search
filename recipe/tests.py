import inspect
from django.db import connection, reset_queries
from django.test import TestCase, override_settings
from .models import Ingredient, Recipe


class RecipeTestCase(TestCase):
    def setUp(self):
        ingredients = [
            Ingredient.objects.create(name='test50', kcal=50),
            Ingredient.objects.create(name='test11', kcal=11)
        ]
        instance = Recipe.objects.create(name='recipe1')
        instance.ingredients.add(*ingredients)

    @override_settings(DEBUG=True)
    def test_calc_kcal(self):
        reset_queries()
        recipe1 = Recipe.objects.filter(name='recipe1').prefetch_related('ingredients').first()
        recipe1.calc_kcal()
        test_kcal = 0
        for i in recipe1.ingredients.all():
            test_kcal += i.kcal
        self.assertTrue(recipe1.kcal, test_kcal)
        print(f'{inspect.currentframe().f_code.co_name} : query count : {len(connection.queries)}')
        for q in connection.queries:
            print(q)
