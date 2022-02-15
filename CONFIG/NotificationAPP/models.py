from django.db import models
from UserAPP.models import ModelUser
from PostAPP.models import ModelPost
from django.utils.crypto import get_random_string

def create_new_ref_number():
    return "notif"+str(get_random_string(25))

class ModelNotification(models.Model):
    NOTIFICATION_TYPE = (
        ("1", "like"),
        ("2", "follow"),
        ("3", "followrequest")
    )
    receiver_user    = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Alan kullanıcı",related_name="notifications")
    sender_user      = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Gönderen Kullanıcı")
    notificationType = models.CharField(choices=NOTIFICATION_TYPE,max_length=15)
    post             = models.ForeignKey(ModelPost,on_delete=models.CASCADE,verbose_name="Post",blank=True,null=True)
    createdDate      = models.DateTimeField(auto_now_add=True)
    isRead           = models.BooleanField(default=False)
    unique_id        = models.CharField(max_length=30, default=create_new_ref_number, editable=False, unique=True)

    class Meta:
        verbose_name        = "Bildirim"
        verbose_name_plural = "Bildirimler"
        db_table            = "Notifications"

class ModelRequest(models.Model):
    receiver_user = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Alan Kullanıcı",related_name="requests")
    sender_user   = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Gönderen Kullanıcı")

    class Meta:
        verbose_name        = "İstek"
        verbose_name_plural = "İstekler"
        db_table            = "Requests"



