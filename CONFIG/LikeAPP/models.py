from django.db import models
from UserAPP.models import ModelUser
from CommentAPP.models import ModelComment
from PostAPP.models import ModelPost
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

class ModelCommentLike(models.Model):
    user    = models.ForeignKey(ModelUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(ModelComment,on_delete=models.CASCADE,related_name="likes")

    def __str__(self):
        return f"{self.user.username} {self.comment}"

    class Meta:
        verbose_name        = "Yorum Beğeni"
        verbose_name_plural = "Yorum Beğenileri"
        db_table            = "CommentLikes"

@receiver(post_save,sender=ModelCommentLike)
def whenLikeComment(sender,instance,*args,**kwargs):
    isLiked = ModelCommentLike.objects.filter(user=instance.user,comment=instance.comment)
    # Eğer kullanıcı yorumu beğenmiş ise veritabanından beğeniyi siliyoruz
    if isLiked.count()==2:
        isLiked.delete()

class ModelPostLike(models.Model):
    user = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    post = models.ForeignKey(ModelPost,on_delete=models.CASCADE,related_name="likes")

    def __str__(self):
        return f"{self.user.username} {self.post.title}"

    class Meta:
        verbose_name        = "Post Beğeni"
        verbose_name_plural = "Post Beğenileri"
        db_table            = "PostLikes"

@receiver(post_save,sender=ModelPostLike)
def whenLikePost(sender,instance,*args,**kwargs):
    isLiked = ModelPostLike.objects.filter(user=instance.user,post=instance.post)
    # Eğer kullanıcı postu beğenmiş ise beğeniyi veritabanından siliyoruz
    if isLiked.count()==2:
        isLiked.delete()