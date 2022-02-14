from django.db import models
from UserAPP.models import ModelUser
from PostAPP.models import ModelPost
from django.utils.crypto import get_random_string

def create_new_ref_number():
    return str(get_random_string(25))

class ModelComment(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Yorumu Atan")
    unique_id   = models.CharField(max_length=100,unique=True,blank=True,default=create_new_ref_number,editable=False)
    text        = models.CharField(max_length=200,verbose_name="Yorum içeriği")
    post        = models.ForeignKey(ModelPost,on_delete=models.CASCADE,verbose_name="Post",related_name="comments")
    parent      = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return f"{self.user.username} {self.unique_id}"

    @property
    def any_children(self):
        # Yorumun herhangi bir alt yorumunun olup olmadığını True false olarak döndürür
        return ModelComment.objects.filter(parent=self).exists()

    def children(self):
        # Yorumun alt yorumlarını döndüren method
        return ModelComment.objects.filter(parent=self)

    def delete_all_children(self):
        # Bir yorum silinirken onun altındaki diğer yorumları da siler
        ModelComment.objects.filter(parent=self).delete()

    class Meta:
        verbose_name        = "Yorum"
        db_table            = "Comments"
        verbose_name_plural = "Yorumlar"
