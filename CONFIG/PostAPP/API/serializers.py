from rest_framework import serializers
from PostAPP.models import ModelPost
from datetime import datetime


class SerializerPostCreateDelete(serializers.ModelSerializer):   # Post oluşturma serializer'ı
    class Meta:
        model  = ModelPost
        fields = ("title","images")

class SerializerOwnPostList(serializers.ModelSerializer):         # Kullanıcı kendi postlarını görüntülediği serializer
    createdDate = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelPost
        fields = ("title","images","createdDate","unique_id")

class SerializerFollowersPostList(serializers.ModelSerializer):    # takipçilerimizin postlarının listelendiği serializer
    createdDate = serializers.SerializerMethodField()
    username    = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.username

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model  = ModelPost
        fields = ("username","title","images","createdDate","unique_id")

class SerializerUserPostList(serializers.ModelSerializer):   # herhangi bir kullanıcının postlarını göstermeye yarar
    createdDate  = serializers.SerializerMethodField()
    modifiedDate = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_modifiedDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    class Meta:
        model = ModelPost
        fields = ("title", "images", "createdDate","modifiedDate", "unique_id")

class SerializerPostUpdate(serializers.ModelSerializer):  # Postu güncellediğimiz serializer
    class Meta:
        model  = ModelPost
        fields = ("title",)


