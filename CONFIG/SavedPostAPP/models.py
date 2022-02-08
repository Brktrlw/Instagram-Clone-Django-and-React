from django.db import models
from UserAPP.models import ModelUser
from PostAPP.models import ModelPost
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver


def create_new_ref_number():
    return str(get_random_string(25))

class ModelSavedPost(models.Model):
    user      = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",related_name="savedposts")
    post      = models.ForeignKey(ModelPost,on_delete=models.CASCADE,verbose_name="Post")
    savedDate = models.DateTimeField(auto_now_add=True,verbose_name="Kaydetme Tarihi")
    unique_id = models.CharField(max_length=30,default=create_new_ref_number,editable=False, unique=True)

    class Meta:
        verbose_name        = "Kaydedilmiş Post"
        verbose_name_plural = "Kaydedilmiş Postlar"
        db_table            = "SavedPosts"
        ordering            = ("-savedDate",)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save,sender=ModelSavedPost)
def whenSavingPost(sender,instance,*args,**kwargs):
    isSaved = ModelSavedPost.objects.filter(user=instance.user,post=instance.post)
    # Eğer kullanıcı postu zaten kaydetmiş ise veritabanından kayıtlı postu kullanıcıdan siliyoruz
    if isSaved.count()==2:
        isSaved.delete()




