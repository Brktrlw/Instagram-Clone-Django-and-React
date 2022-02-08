from django.db import models
from UserAPP.models import ModelUser
from PostAPP.models import ModelPost

class ModelComment(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Yorumu Atan")
    text        = models.CharField(max_length=200,verbose_name="Yorum içeriği")
    post        = models.ForeignKey(ModelPost,on_delete=models.CASCADE,verbose_name="Post",related_name="comments")
    parent      = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return f"{self.user.username} - {self.post.title} + {self.text}"

    @property
    def any_children(self):
        return ModelComment.objects.filter(parent=self).exists()

    def children(self):
        return ModelComment.objects.filter(parent=self)

    class Meta:
        verbose_name        = "Yorum"
        db_table            = "Comments"
        verbose_name_plural = "Yorumlar"
