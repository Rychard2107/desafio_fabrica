from urllib import request
from django.shortcuts import render, redirect
from .forms import Recipesnewpost
from .models import RecipesPost

def home(request):
    data = {}
    data['receitas'] = RecipesPost.objects.all()
    return render(request, 'recipes/home.html', data)


def create(request):
    form = Recipesnewpost(request.POST or None)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('home')
    data['form'] = form
    return render(request, 'recipes/create.html', data)


def update(request, pk):
    objeto = RecipesPost.objects.get(pk=pk)
    form = Recipesnewpost(request.POST or None, instance=objeto)
    data = {}
    data['objeto'] = objeto
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'blog/create.html', data)


def delete(request, pk):
    objeto = RecipesPost.objects.get(pk=pk)
    objeto.delete()
    return redirect('home')