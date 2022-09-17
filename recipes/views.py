from django.shortcuts import render
from .models import RecipesPost

def home(request):
    data = {}
    data['receitas'] = RecipesPost.objects.all()
    return render(request, 'recipes/home.html', data)
