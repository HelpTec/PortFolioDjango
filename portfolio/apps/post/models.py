from django.db import models
from apps.bio.models import Bio


class Post(models.Model):
    texto = models.CharField(max_length=200)
    bio = models.ForeignKey(Bio, 
                                on_delete= models.CASCADE, 
                                related_name= "Post",
                                blank= True, 
                                null= True)