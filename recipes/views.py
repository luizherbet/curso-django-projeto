from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipe = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes' : recipe, "name": "Recipes"})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={'recipe' : make_recipe(), "name":"Recipes", "is_detail_page":True})