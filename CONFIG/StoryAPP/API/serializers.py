from rest_framework import serializers
from StoryAPP.models import ModelStory
from datetime import datetime


class SerializerUserStories(serializers.ModelSerializer):
    # Kullanıcının adına göre hikayelerini listeleyen serializer
    username    = serializers.CharField(source="user.username")
    createdDate = serializers.SerializerMethodField()

    def get_createdDate(self,obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelStory
        fields = ("username","image","createdDate")



