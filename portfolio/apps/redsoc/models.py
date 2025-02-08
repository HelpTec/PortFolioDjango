from django.db import models
from apps.persona.models import Persona

class RedSoc(models.Model):
    nombre = models.CharField(max_length = 255)
    url = models.CharField(max_length = 500)
    persona = models.ForeignKey(Persona, 
                                on_delete= models.CASCADE, 
                                related_name= "Redsoc",
                                blank= True, 
                                null= True)