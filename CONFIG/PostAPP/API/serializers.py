from rest_framework import serializers
from PostAPP.models import ModelPost
from datetime import datetime
from LikeAPP.models import ModelPostLike
from UserAPP.API.serializers import SerializerUserSimpleInfo
from CONFIG.tools import LOCAL_IP,PORT_NUMBER

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
    createdDate = serializers.SerializerMethodField()
    isLiked = serializers.SerializerMethodField()
    ratio = serializers.SerializerMethodField()
    modifiedDate = serializers.SerializerMethodField()
    user=SerializerUserSimpleInfo()

    def get_ratio(self, obj):
        try:
            return obj.images.width / obj.images.height
        except:
            return None

    def get_modifiedDate(self, obj):
        tarih = datetime.strftime(obj.modifiedDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_isLiked(self, obj):
        return ModelPostLike.objects.filter(post=obj, user=self.context["request"].user).exists()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelPost
        fields = ("user","unique_id","title","images","isLiked","ratio","createdDate","modifiedDate")

class SerializerPostUpdate(serializers.ModelSerializer):
    # Postu güncellediğimiz serializer
    class Meta:
        model  = ModelPost
        fields = ("title",)

class SerializerUserPostList(serializers.ModelSerializer):
    #herhangi bir kullanıcının kullanıcı adına göre postlarını göstermeye yarar
    createdDate  = serializers.SerializerMethodField()
    modifiedDate = serializers.SerializerMethodField()
    #isLiked      = serializers.SerializerMethodField()
    ratio        = serializers.SerializerMethodField()
    user         = SerializerUserSimpleInfo()

    #def get_isLiked(self,obj):
    #    return ModelPostLike.objects.filter(post=obj,user=self.context["request"].user).exists()

    def get_ratio(self,obj):
        try:
            return obj.images.width / obj.images.height
        except:
            return None

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_modifiedDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model = ModelPost
        #fields = ("user","unique_id","title", "images","isLiked","ratio", "createdDate","modifiedDate")
        fields = ("user","unique_id","title", "images","ratio", "createdDate","modifiedDate")




