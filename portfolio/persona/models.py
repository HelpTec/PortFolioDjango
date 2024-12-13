from django.db import models

class Persona(models.Model):
    user = models.OneToOneField(
        "Usuario",
        on_delete=models.CASCADE,
        related_name= "persona",
        blank=True,
        null=True)
    nombres = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField
    telefono = models.IntegerField(max_length=20)
    mail = models.CharField(max_length=30)
    redes = models.ForeignKey(
        "RedSoc",
        on_delete=models.CASCADE,
        related_name= "redpersona",
        blank=True,
        null=True)
    def __str__(self):
        return f"{self.nombres} {self.apellido}"
