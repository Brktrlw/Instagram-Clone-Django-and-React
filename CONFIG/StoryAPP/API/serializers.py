from rest_framework import serializers
from StoryAPP.models import ModelStory
from datetime import datetime
from StoryAPP.models import ModelStoryRead

class SerializerUserStories(serializers.ModelSerializer):
    # Kullanıcının adına göre hikayelerini listeleyen serializer
    username    = serializers.CharField(source="user.username")
    createdDate = serializers.SerializerMethodField()
    isRead      = serializers.SerializerMethodField()

    def get_isRead(self,obj):
        print(obj)
        user=self.context["request"].user # hikayeyi görüntüleyen kullanıcı
        #readObject = ModelStoryRead.objects.filter(user=user).exists()
        #if not readObject:
        #    ModelStoryRead.objects.create(user=user)


    def get_createdDate(self,obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelStory
        fields = ("username","image","createdDate","isRead")



