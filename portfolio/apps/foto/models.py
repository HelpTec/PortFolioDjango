from django.db import models

class Foto(models.Model):
    foto = models.ImageField(upload_to='fotos/')
    def __str__(self):
        return f"{self.foto.name}"