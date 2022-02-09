from rest_framework import serializers
from CommentAPP.models import ModelComment
from datetime import datetime
from UserAPP.API.serializers import SerializerUserSimpleInfo
from LikeAPP.models import ModelCommentLike

class SerializerCommentListByPost(serializers.ModelSerializer):
    #Postun yorumlarını listelediğimiz serializer
    replies     = serializers.SerializerMethodField()
    createdDate = serializers.SerializerMethodField()
    user        = SerializerUserSimpleInfo()
    isLiked     = serializers.SerializerMethodField()

    def get_isLiked(self,obj):
        # isteği atan kullanıcı yorumu beğenmiş mi
        return ModelCommentLike.objects.filter(user=self.context.get("request").user,comment=obj).exists()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_replies(self, obj):
        # Yorumların alt yorumlarını bulmamızı sağlayan method
        if obj.any_children:
            return SerializerCommentListByPost(obj.children(),many=True,context={"request":self.context["request"]}).data

    class Meta:
        model  = ModelComment
        fields = ("user","text","isLiked","createdDate","unique_id","replies",)

class SerializerCreateComment(serializers.ModelSerializer):
    # Yorum oluşturma view
    class Meta:
        model  = ModelComment
        fields = ("text","parent",)

    def validate(self, attrs):
        # Child yorumun postu ile parent yorumun postu aynı mı kontrol işlemi
        if attrs["parent"]:
            if attrs["parent"].post != self.context["view"].kwargs["postunique_id"]:
                raise serializers.ValidationError("Postlar farklı")
        return attrs


class SerializerDeleteComment(serializers.ModelSerializer):
    # Yorum silme serializer
    class Meta:
        model  = ModelComment
        fields = ("user",)