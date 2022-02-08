from django.db import models
from UserAPP.models import ModelUser
from django.utils.crypto import get_random_string

def create_new_ref_number():
    return str(get_random_string(30))

class ModelPost(models.Model):
    user         = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="posts")
    createdDate  = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    modifiedDate = models.DateTimeField(auto_now=True,verbose_name="Güncellenme Tarihi")
    title        = models.CharField(max_length=200,verbose_name="Başlık")
    images       = models.FileField(upload_to="Posts",null=True,blank=True)
    unique_id    = models.CharField(max_length=30,default=create_new_ref_number,editable=False, unique=True)

    def __str__(self):
        return f"{self.user.username} {self.title}---{self.unique_id}"

    class Meta:
        db_table            = "Posts"
        verbose_name        = "Gönderi"
        verbose_name_plural = "Gönderiler"