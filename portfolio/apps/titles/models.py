from django.db import models
from apps.persona.models import Persona

class Titles(models.Model):
    nombre = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, on_delete= models.CASCADE, related_name= "Titles",blank= True, null= True)

    def __str__(self):
        return f"{self.nombre}"
