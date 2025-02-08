from django.db import models
from apps.persona.models import Persona

class Trabajos(models.Model):
    nombre = models.CharField(max_length=100)
    urlTrabajo = models.CharField(max_length=300, null= True, blank= True)
    avatarImg = models.CharField(max_length=300)
    persona = models.ForeignKey(Persona, 
                                on_delete= models.CASCADE, 
                                related_name= "Trabajos",
                                blank= True, 
                                null= True)