from rest_framework import serializers
from StoryAPP.models import ModelStory
from datetime import datetime
from CONFIG.tools import LOCAL_IP,PORT_NUMBER

class SerializerUserStories(serializers.ModelSerializer):
    # Kullanıcının adına göre hikayelerini listeleyen serializer
    username    = serializers.CharField(source="user.username")
    createdDate = serializers.SerializerMethodField()

    def get_createdDate(self,obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelStory
        fields = ("username","image","createdDate",)


class SerializerHomePageStories(serializers.ModelSerializer):
    username    = serializers.SerializerMethodField()
    profilePhoto = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.username

    def get_profilePhoto(self,obj):
        if obj.user.profilePhoto:
            return obj.get_image_url()

    class Meta:
        model = ModelStory
        fields=("username","profilePhoto")
