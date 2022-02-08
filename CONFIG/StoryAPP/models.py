from django.db import models
from UserAPP.models import ModelUser



class ModelStory(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="stories",verbose_name="Kullanıcı")
    image       = models.FileField(upload_to="Stories",)
    createdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = "Hikaye"
        verbose_name_plural = "Hikayeler"
        db_table            = "Stories"

    def __str__(self):
        return f"{self.user.username}"

