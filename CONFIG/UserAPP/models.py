from django.db import models
from django.contrib.auth.models import AbstractUser

class ModelUser(AbstractUser):
    profilePhoto = models.ImageField(upload_to="profilePhoto",blank=True,null=True,verbose_name="Profil Fotoğrafı")
    private      = models.BooleanField(default=False,verbose_name="Gizli Hesap mı")
    biography    = models.CharField(max_length=100,verbose_name="Biyogrofi",null=True,blank=True)
    def __str__(self):
        return self.username

class ModelFollower(models.Model):
    follower  = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Takip edilen",related_name="followers")
    following = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Takip eden",related_name="followings")
    class Meta:
        verbose_name        = "Takip"
        db_table            = "Follower"
        verbose_name_plural = "Takip"

    def __str__(self):
        return f"Takip Eden: {self.following} Takip Edilen: {self.follower}"

