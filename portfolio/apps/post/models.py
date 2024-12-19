from django.db import models
from apps.titles.models import Titles
from apps.foto.models import Foto

class Post(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    foto = models.ForeignKey(
        Foto,
        on_delete=models.CASCADE,
        blank=True,
        null=True)