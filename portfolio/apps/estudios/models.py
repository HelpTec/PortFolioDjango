from django.db import models

class Estudios(models.Model):
    titulo = models.CharField(max_length=50)
    establecimiento = models.CharField(max_length=50)
    urlEstablecimiento = models.CharField(max_length=100)
    inicio = models.DateField()
    final = models.DateField(null=True, blank=True)
    avatarImg = models.CharField(max_length=100)

