from django.db import models
from apps.persona.models import Persona

class Master(models.Model):
    hardcoded = models.BooleanField(default=False)
    persona = models.ForeignKey(Persona, 
                                on_delete= models.CASCADE, 
                                null= True, blank=True)