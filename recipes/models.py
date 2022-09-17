from django.db import models


class RecipesPost(models.Model):
    titulo = models.CharField(max_length=50,
        verbose_name="Título da receita", unique=True)
    datatime = models.DateTimeField(verbose_name="Data e hora")
    mododepreparo = models.TextField(verbose_name="Modo de preparo")
    ingrediente = models.TextField(verbose_name="Ingredientes")
    def __str__(self):
        return self.titulo
    