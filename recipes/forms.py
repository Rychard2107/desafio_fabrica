from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import RecipesPost

class Recipesnewpost(ModelForm):
    class Meta:
        model = RecipesPost
        fields = ['titulo', 'datatime', 'ingrediente', 'mododepreparo']