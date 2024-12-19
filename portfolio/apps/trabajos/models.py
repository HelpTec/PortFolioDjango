from django.db import models

class Trabajos(models.Model):
    ocupacion = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    urlEmpresa = models.CharField(max_length=100)
    inicio = models.DateField()
    final = models.DateField(null=True, blank=True)
    avatarImg = models.CharField(max_length=100)
