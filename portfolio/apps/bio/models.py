from django.db import models
from apps.persona.models import Persona

class Bio(models.Model):
    persona = models.ForeignKey(Persona, 
                                on_delete= models.CASCADE, 
                                related_name= "Bio",
                                blank= True, 
                                null= True)
    fotoPerf = models.CharField(max_length=300, blank= True, null= True)