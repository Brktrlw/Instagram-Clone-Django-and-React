from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
from CONFIG.tools import LOCAL_IP,PORT_NUMBER


class ModelUser(AbstractUser):
    date_from    = timezone.now() - datetime.timedelta(days=1)
    profilePhoto = models.ImageField(upload_to="profilePhoto",blank=True,null=True,verbose_name="Profil Fotoğrafı")
    private      = models.BooleanField(default=False,verbose_name="Gizli Hesap mı")
    biography    = models.CharField(max_length=100,verbose_name="Biyogrofi",null=True,blank=True)

    def __str__(self):
        return self.username

    def get_current_stories(self):
        # kullanıcının o anki mevcut hikayelerini döndürür
        return self.stories.filter(user=self,createdDate__gte=self.date_from)

    def is_any_story(self):
        # kullanıcının o an aktif halde olan hikayesi var mı yok mu True/False döndürür
        return self.stories.filter(user=self,createdDate__gte=self.date_from).exists()

    def get_profile_photo_url(self):
        return "http://"+LOCAL_IP+":"+PORT_NUMBER+self.profilePhoto.url

class ModelFollower(models.Model):
    follower  = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Takip edilen",related_name="followers")
    following = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Takip eden",related_name="followings")
    class Meta:
        verbose_name        = "Takip"
        db_table            = "Follower"
        verbose_name_plural = "Takip"

    def __str__(self):
        return f"Takip Eden: {self.following} Takip Edilen: {self.follower}"
