from rest_framework import serializers
from SavedPostAPP.models import ModelSavedPost
from PostAPP.models import ModelPost
from datetime import datetime
from LikeAPP.models import ModelPostLike


class SerializerSavedPost(serializers.ModelSerializer):
    username    = serializers.CharField(source="user.username")
    createdDate = serializers.SerializerMethodField()
    totalLike   = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_totalLike(self,obj):
        return ModelPostLike.objects.filter(post__unique_id=obj.unique_id).count()

    class Meta:
        model  = ModelPost
        fields = ("username","createdDate","images","unique_id","totalLike")

class SerializerSavedUserPost(serializers.ModelSerializer):
    post = SerializerSavedPost()
    class Meta:
        model  = ModelSavedPost
        fields = ("post",)


