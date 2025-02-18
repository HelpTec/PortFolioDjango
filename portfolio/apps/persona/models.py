from django.db import models
from apps.usuario.models import Usuario

class Persona(models.Model):
    user = models.OneToOneField(
        Usuario,
        on_delete = models.CASCADE,
        related_name= "persona",
        blank=True,
        null=True)
    nombres = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField(blank= True, null= True)
    telefono = models.IntegerField(blank= True, null= True)
    mail = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nombres} {self.apellido}"
