from rest_framework import serializers
from CommentAPP.models import ModelComment
from datetime import datetime

class SerializerCommentListByPost(serializers.ModelSerializer):   #Postun yorumlarını listelediğimiz serializer
    user        = serializers.CharField(source="user.username")
    replies     = serializers.SerializerMethodField()
    createdDate = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_replies(self, obj):
        if obj.any_children:
            return SerializerCommentListByPost(obj.children(),many=True).data

    class Meta:
        model  = ModelComment
        fields = ("user","text","createdDate","unique_id","replies")

class SerializerCreateComment(serializers.ModelSerializer):   # yorum oluşturma view
    class Meta:
        model  = ModelComment
        fields = ("text","parent",)

    def validate(self, attrs): # child yorumun postu ile parent yorumun postu aynı mı kontrol işlemi
        if attrs["parent"]:
            if attrs["parent"].post != self.context["view"].kwargs["postunique_id"]:
                raise serializers.ValidationError("Postlar farklı")
        return attrs


class SerializerDeleteComment(serializers.ModelSerializer):
    class Meta:
        model  = ModelComment
        fields = ("user",)