from rest_framework import serializers
from PostAPP.models import ModelPost
from datetime import datetime
from LikeAPP.models import ModelPostLike
from UserAPP.API.serializers import SerializerUserSimpleInfo
from django.utils.timesince import timesince

class SerializerPostCreateDelete(serializers.ModelSerializer):
    # Post oluşturma serializer'ı
    class Meta:
        model  = ModelPost
        fields = ("title","images")

class SerializerOwnPostList(serializers.ModelSerializer):
    # Kullanıcı kendi postlarını görüntülediği serializer
    createdDate  = serializers.SerializerMethodField()
    isLiked      = serializers.SerializerMethodField()
    ratio        = serializers.SerializerMethodField()
    modifiedDate = serializers.SerializerMethodField()
    image        = serializers.SerializerMethodField()

    def get_image(self,obj):
        return obj.get_image_url()

    def get_ratio(self,obj):
        try:
            return obj.images.width / obj.images.height
        except:
            return None
    def get_modifiedDate(self, obj):
        tarih = datetime.strftime(obj.modifiedDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_isLiked(self,obj):
        return ModelPostLike.objects.filter(post=obj,user=self.context["request"].user).exists()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelPost
        fields = ("unique_id","title","image","isLiked","ratio","createdDate","modifiedDate")

class SerializerFollowersPostList(serializers.ModelSerializer):
    # takipçilerimizin postlarının anasayfada listelendiği serializer
    isLiked      = serializers.SerializerMethodField()
    ratio        = serializers.SerializerMethodField()
    user         = SerializerUserSimpleInfo()
    likeCount    = serializers.SerializerMethodField()
    commentCount = serializers.SerializerMethodField()
    postImage    = serializers.SerializerMethodField()
    createdDate  = serializers.SerializerMethodField()

    def get_createdDate(self,obj):
        return obj.time_format()

    def get_postImage(self,obj):
        return obj.get_image_url()

    def get_commentCount(self,obj):
        return obj.comments.all().count()

    def get_likeCount(self,obj):
        return obj.likes.all().count()

    def get_ratio(self, obj):
        try:
            return obj.images.width / obj.images.height
        except:
            return None

    def get_isLiked(self, obj):
        return ModelPostLike.objects.filter(post=obj, user=self.context["request"].user).exists()

    class Meta:
        model  = ModelPost
        fields = ("user","unique_id","title","postImage","isLiked","ratio","createdDate","likeCount","commentCount")

class SerializerPostUpdate(serializers.ModelSerializer):
    # Postu güncellediğimiz serializer
    class Meta:
        model  = ModelPost
        fields = ("title",)

class SerializerUserPostList(serializers.ModelSerializer):
    #herhangi bir kullanıcının kullanıcı adına göre postlarını göstermeye yarar
    createdDate  = serializers.SerializerMethodField()
    isLiked      = serializers.SerializerMethodField()
    ratio        = serializers.SerializerMethodField()
    likeCount    = serializers.SerializerMethodField()
    commentCount = serializers.SerializerMethodField()

    def get_createdDate(self,obj):
        return obj.time_format()

    def get_commentCount(self,obj):
        return obj.comments.all().count()

    def get_likeCount(self,obj):
        return obj.likes.all().count()

    def get_isLiked(self,obj):
        return ModelPostLike.objects.filter(post=obj,user=self.context["request"].user).exists()

    def get_ratio(self,obj):
        try:
            return obj.images.width / obj.images.height
        except:
            return None

    class Meta:
        model = ModelPost
        fields = ("unique_id","title", "images","ratio","isLiked","likeCount","commentCount" ,"createdDate",)




