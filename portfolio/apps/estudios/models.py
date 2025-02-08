from django.db import models
from apps.persona.models import Persona

class Estudios(models.Model):
    titulo = models.CharField(max_length=50)
    establecimiento = models.CharField(max_length=50)
    urlEstablecimiento = models.CharField(max_length=100)
    inicio = models.DateField()
    final = models.DateField(null=True, blank=True)
    avatarImg = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, 
                                on_delete= models.CASCADE, 
                                related_name= "Estudios",
                                blank= True, 
                                null= True)

