from django.db import models
from UserAPP.models import ModelUser
from django.utils.crypto import get_random_string
from CONFIG.tools import LOCAL_IP,PORT_NUMBER
from django.utils.timesince import timesince

def create_new_ref_number():
    return str("story")+str(get_random_string(30))

class ModelStory(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="stories",verbose_name="Kullanıcı")
    image       = models.FileField(upload_to="Stories",)
    createdDate = models.DateTimeField(editable=False,auto_now_add=True)
    unique_id   = models.CharField(max_length=35,default=create_new_ref_number,editable=False, unique=True)

    def get_format_createdDate(self):
        return timesince(self.createdDate)+str(" önce")

    class Meta:
        verbose_name        = "Hikaye"
        verbose_name_plural = "Hikayeler"
        db_table            = "Stories"

    def __str__(self):
        return f"{self.user.username}"

    def get_image_url(self):
        return "http://"+LOCAL_IP+":"+PORT_NUMBER+self.image.url


class ModelStoryRead(models.Model):
    user  = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Gören Kullanıcı")
    story = models.ForeignKey(ModelStory,on_delete=models.CASCADE,related_name="seeingusers",verbose_name="Hikaye")

    def __str__(self):
        return self.story.unique_id

    class Meta:
        db_table="StoryRead"