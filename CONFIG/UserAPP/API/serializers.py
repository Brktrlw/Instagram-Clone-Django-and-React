from rest_framework import serializers
from UserAPP.models import ModelUser,ModelFollower



class SerializerUserFollowers(serializers.ModelSerializer):
    follower = serializers.CharField(source="following.username")

    class Meta:
        model  = ModelFollower
        fields = ("follower",)

class SerializerUserFollowings(serializers.ModelSerializer):
    following = serializers.CharField(source="follower.username")
    class Meta:
        model  = ModelFollower
        fields = ("following",)

class SerializerUserProfile(serializers.ModelSerializer):
    # Kullanıcının profil bilgilerini gönderdiğimiz serializer
    totalFollowers  = serializers.SerializerMethodField()
    totalFollowings = serializers.SerializerMethodField()
    isAnyStory      = serializers.SerializerMethodField()

    def get_isAnyStory(self,obj):
        return obj.is_any_story()

    def get_totalFollowers(self,obj):
        return obj.followers.count()

    def get_totalFollowings(self,obj):
        return obj.followings.count()

    class Meta:
        model  = ModelUser
        fields = ("username","totalFollowers","totalFollowings","biography","isAnyStory","profilePhoto")


class SerializerUserSimpleInfo(serializers.ModelSerializer):
    isAnyStory = serializers.SerializerMethodField()

    def get_isAnyStory(self,obj):
        return obj.is_any_story()
    class Meta:
        model  = ModelUser
        fields = ("username","isAnyStory")

