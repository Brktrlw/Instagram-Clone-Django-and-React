from django.db import models
from UserAPP.models import ModelUser
from django.utils.crypto import get_random_string
from CONFIG.tools import LOCAL_IP,PORT_NUMBER
from django.contrib.humanize.templatetags.humanize import naturalday,naturaltime

def create_new_ref_number():
    return str(get_random_string(30))

class ModelPost(models.Model):
    user         = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="posts")
    createdDate  = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    modifiedDate = models.DateTimeField(auto_now=True,verbose_name="Güncellenme Tarihi")
    title        = models.CharField(max_length=200,verbose_name="Başlık")
    images       = models.ImageField(upload_to="Posts",null=True,blank=True)
    unique_id    = models.CharField(max_length=30,default=create_new_ref_number,editable=False, unique=True)

    def __str__(self):
        return f"{self.user.username} {self.title}---{self.unique_id}"

    def get_image_url(self):
        return "http://"+LOCAL_IP+":"+PORT_NUMBER+self.images.url

    def time_format(self):
        format=naturaltime(self.createdDate)
        if "days," in format:
            format = self.createdDate.strftime("%a %d %Y")
        elif "day," in format:
            format = naturalday(format)
        elif "minutes" in format:
            format=format.replace("minutes","m")
        elif "minute" in format:
            format=format.replace("minute","m")
        elif "hours" in format:
            format=format.replace("hours","h")
        elif "hour" in format:
            format=format.replace("hour","h")
        return format.replace(" ","")
    class Meta:
        db_table            = "Posts"
        verbose_name        = "Gönderi"
        verbose_name_plural = "Gönderiler"