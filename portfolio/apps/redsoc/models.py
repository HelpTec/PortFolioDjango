from django.db import models

class RedSoc(models.Model):
    nombre = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)