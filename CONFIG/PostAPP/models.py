from django.db import models
from UserAPP.models import ModelUser

class ModelPost(models.Model):
    user         = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="posts")
    createdDate  = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    title        = models.CharField(max_length=200,verbose_name="Başlık")
    image        = models.FileField(upload_to="Posts")

