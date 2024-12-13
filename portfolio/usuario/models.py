from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    persona = models.OneToOneField("persona",
                                   on_delete= models.CASCADE,
                                   related_name="persona",
                                   blank= True,
                                   null= True)
    username = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.username}"
