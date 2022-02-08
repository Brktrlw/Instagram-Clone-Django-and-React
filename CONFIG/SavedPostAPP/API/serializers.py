from rest_framework import serializers
from SavedPostAPP.models import ModelSavedPost
from PostAPP.models import ModelPost
from datetime import datetime
from LikeAPP.models import ModelPostLike


class SerializerSavedPost(serializers.ModelSerializer):
    # kayıtlı postları serilize etmek için kullandığımız serializer
    username     = serializers.CharField(source="user.username")
    createdDate  = serializers.SerializerMethodField()
    totalLike    = serializers.SerializerMethodField()
    modifiedDate = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_modifiedDate(self, obj):
        tarih = datetime.strftime(obj.modifiedDate, '%H:%M:%S %d/%m/%Y')
        return str(tarih)

    def get_totalLike(self,obj):
        return ModelPostLike.objects.filter(post__unique_id=obj.unique_id).count()

    class Meta:
        model  = ModelPost
        fields = ("username","title","images","createdDate","modifiedDate","totalLike","unique_id",)


class SerializerSavedUserPost(serializers.ModelSerializer):
    # Kullanıcının kayıtlı postlarını listelediğimiz view
    post = SerializerSavedPost()
    class Meta:
        model  = ModelSavedPost
        fields = ("post",)


class SerializerCreateSavePost(serializers.ModelSerializer):
    # Savedlara post eklemek için kullandığımız serializer
    class Meta:
        model  = ModelSavedPost
        fields = ("user",)


