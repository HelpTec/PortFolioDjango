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
    nacimiento = models.DateField
    telefono = models.IntegerField
    mail = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nombres} {self.apellido}"
