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



