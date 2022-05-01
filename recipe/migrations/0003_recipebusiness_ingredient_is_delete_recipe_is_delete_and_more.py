# Generated by Django 4.0.4 on 2022-04-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_kcal'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeBusiness',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('recipe.recipe',),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]