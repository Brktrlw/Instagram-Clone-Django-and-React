from rest_framework import serializers
from StoryAPP.models import ModelStory,ModelStoryRead
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
        fields = ("username","image","createdDate",)


class SerializerHomePageStories(serializers.ModelSerializer):
    # Ana sayfada kullanıcının takip ettiği kişilerin hikayelerini listeler
    username     = serializers.SerializerMethodField()
    profilePhoto = serializers.SerializerMethodField()
    isAllRead     = serializers.SerializerMethodField()

    def get_isAllRead(self,obj):
        # Giriş yapmış kullanıcı bir kullanıcının tüm hikayelerini görüp görmediğini döndürür
        allStories = ModelStory.objects.filter(user=obj.user)
        readObj    = ModelStoryRead.objects.filter(user=self.context["request"].user,story__in=allStories)
        if allStories.count()==readObj.count():
            return True
        return False

    def get_username(self,obj):
        return obj.user.username

    def get_profilePhoto(self,obj):
        if obj.user.profilePhoto:
            return obj.get_image_url()

    class Meta:
        model = ModelStory
        fields=("username","profilePhoto","isAllRead","likeCount")


class SerializerOwnStories(serializers.ModelSerializer):
    # Kullanıcı kendi hikayelerini listeler
    image               = serializers.SerializerMethodField()
    format_createdDate  = serializers.SerializerMethodField()

    def get_image(self,obj):
        return obj.get_image_url() # Model methodu

    def get_format_createdDate(self,obj):
        return obj.get_format_createdDate() # Model methodu

    class Meta:
        model = ModelStory
        fields=("image","unique_id","format_createdDate")

class SerializerCreateReadStory(serializers.ModelSerializer):
    # Herhangi bir hikayeyi okumak için çalıştırdığımız serializer
    unique_id=serializers.CharField(source="story.unique_id")
    class Meta:
        model  = ModelStoryRead
        fields = ("unique_id",)

class SerializerUsersBySeeingStory(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    profilePhoto=serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.username

    def get_profilePhoto(self,obj):
        if obj.user.profilePhoto:
            return obj.user.get_profile_photo_url()
        return None


    class Meta:
        model  = ModelStoryRead
        fields =("username","profilePhoto")

