from django.db import models

class Usuario(models.Model):
    hardcoded = models.BooleanField(default=False)