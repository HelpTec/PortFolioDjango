from django.db import models
from apps.persona.models import Persona

class Tecnologias(models.Model):
    Persona= models.ForeignKey(
        Persona,
        null=True, 
        blank=True,
        related_name= "tecno",
        on_delete=models.CASCADE)
    avatarImg= models.CharField(
        max_length= 250,
        null=True, 
        blank=True,
    )
    nombre= models.CharField(
        max_length= 30,
        null=True, 
        blank=True,
    )
    nivel= models.CharField(
        max_length= 30,
        null=True, 
        blank=True,
    )