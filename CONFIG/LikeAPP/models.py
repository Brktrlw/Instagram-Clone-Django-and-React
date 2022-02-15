from django.db import models
from UserAPP.models import ModelUser
from CommentAPP.models import ModelComment
from PostAPP.models import ModelPost
from django.db.models.signals import post_save
from django.dispatch import receiver
from NotificationAPP.models import ModelNotification

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
    if isLiked.count()==2:
        # Eğer kullanıcı yorumu beğenmiş ise veritabanından beğeniyi siliyoruz
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
def whenPostIsLiked(sender,instance,*args,**kwargs):
    isLiked = ModelPostLike.objects.filter(user=instance.user,post=instance.post)
    notif   = ModelNotification.objects.filter(receiver_user=instance.post.user,post=instance.post,sender_user=instance.user,notificationType="like")
    if isLiked.count()==2:
        # Eğer kullanıcı postu beğenmiş ise beğeniyi ve bildirimi veritabanından siliyoruz
        isLiked.delete()
        notif.delete()
    else:
        if instance.post.user != instance.user:
            # Eğer kullanıcı kendi gönderisini beğeniyorsa bildirim kayıt edilmez
            ModelNotification.objects.create(receiver_user=instance.post.user,post=instance.post,sender_user=instance.user,notificationType=1)
