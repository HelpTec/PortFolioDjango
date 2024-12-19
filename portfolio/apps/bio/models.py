from django.db import models
from apps.estudios.models import Estudios
from apps.trabajos.models import Trabajos

class Bio(models.Model):
    texto = models.CharField(max_length=1000)
    estudios = models.ForeignKey(
        Estudios,
        on_delete= models.CASCADE,
        blank=True,
        null=True)
    trabajos = models.ForeignKey(
        Trabajos,
        on_delete= models.CASCADE, 
        blank=True, 
        null=True)