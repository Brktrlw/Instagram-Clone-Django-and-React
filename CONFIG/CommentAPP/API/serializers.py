from rest_framework import serializers
from CommentAPP.models import ModelComment
from UserAPP.API.serializers import SerializerUserSimpleInfo
from LikeAPP.models import ModelCommentLike
from django.utils.timesince import timesince
from CONFIG.tools import get_last_minute
class SerializerCommentListByPost(serializers.ModelSerializer):
    #Postun yorumlarını listelediğimiz serializer
    replies      = serializers.SerializerMethodField()
    createdDate  = serializers.SerializerMethodField()
    user         = SerializerUserSimpleInfo()
    isLiked      = serializers.SerializerMethodField()
    likeCount    = serializers.SerializerMethodField()
    repliesCount = serializers.SerializerMethodField()

    def get_repliesCount(self,obj):
        return obj.children().count()


    def get_likeCount(self,obj):
        return obj.likes.all().count()

    def get_isLiked(self,obj):
        # isteği atan kullanıcı yorumu beğenmiş mi
        return ModelCommentLike.objects.filter(user=self.context.get("request").user,comment=obj).exists()

    def get_createdDate(self, obj):
        createdDate=get_last_minute(obj.createdDate)
        return createdDate


    def get_replies(self, obj):
        # Yorumların alt yorumlarını bulmamızı sağlayan method
        if obj.any_children:
            return SerializerCommentListByPost(obj.children(),many=True,context={"request":self.context["request"]}).data

    class Meta:
        model  = ModelComment
        fields = ("user","text","isLiked","createdDate","unique_id","likeCount","repliesCount","replies")

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