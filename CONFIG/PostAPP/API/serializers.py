from rest_framework import serializers
from PostAPP.models import ModelPost
from datetime import datetime

class SerializerPostCreateDelete(serializers.ModelSerializer):
    class Meta:
        model  = ModelPost
        fields = ("title","images")

class SerializerOwnPostList(serializers.ModelSerializer):
    createdDate = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    class Meta:
        model  = ModelPost
        fields = ("title","images","createdDate","unique_id")

class SerializerFollowersPostList(serializers.ModelSerializer):
    createdDate = serializers.SerializerMethodField()
    username    = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.username

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    class Meta:
        model  = ModelPost
        fields = ("username","title","images","createdDate","unique_id")


