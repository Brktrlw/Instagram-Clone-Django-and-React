from django.db import models
from UserAPP.models import ModelUser

class TestModel(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı",null=True,blank=True)
    firstName   = models.CharField(max_length=200,verbose_name="İsim",help_text="İsim")
    surName     = models.CharField(max_length=200,verbose_name="Soy isim",help_text="Soy isim")
    description = models.TextField(max_length=500,verbose_name="İçerik",help_text="İçerik")

    def __str__(self):
        return str(self.id)