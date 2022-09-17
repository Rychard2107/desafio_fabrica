from django.db import models


class RecipesPost(models.Model):
    titulo = models.CharField(max_length=50,
        verbose_name="Título da receita", unique=True)
    datatime = models.DateTimeField(auto_now=True)
    mododepreparo = models.TextField(verbose_name="Modo de preparo",default=True)
    ingrediente = models.TextField(default=True)
    def __str__(self):
        return self.titulo
    