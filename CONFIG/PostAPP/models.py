from django.db import models
from UserAPP.models import ModelUser
import uuid

class ModelPost(models.Model):
    user         = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="posts")
    createdDate  = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    title        = models.CharField(max_length=200,verbose_name="Başlık")
    images       = models.FileField(upload_to="Posts",null=True,blank=True)
    unique_id    = models.UUIDField(default=uuid.uuid4,editable=False, unique=True)

    def __str__(self):
        return f"{self.user.username} {self.title}---{self.unique_id}"

    class Meta:
        db_table            = "Posts"
        verbose_name        = "Gönderi"
        verbose_name_plural = "Gönderiler"