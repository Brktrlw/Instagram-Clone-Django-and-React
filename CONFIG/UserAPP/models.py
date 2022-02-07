from django.db import models
from django.contrib.auth.models import AbstractUser



class ModelUser(AbstractUser):
    profilePhoto = models.ImageField(upload_to="profilePhoto",blank=True,null=True,verbose_name="Profil Fotoğrafı")

    def __str__(self):
        return self.username
