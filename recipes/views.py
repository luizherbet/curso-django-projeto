from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name' : 'Zama',})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={'name' : 'Recipe',})