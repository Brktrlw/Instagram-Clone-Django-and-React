from rest_framework import serializers
from UserAPP.models import ModelUser,ModelFollower
import datetime
from StoryAPP.models import ModelStory
from django.utils import timezone


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
        # son 24 saatte hikayesi olup olmadığını kontrol eder
        date_from               = timezone.now() - datetime.timedelta(days=1)
        isCurrentStoryAvilable  = ModelStory.objects.filter(user=obj,createdDate__gte=date_from).exists()
        return isCurrentStoryAvilable


    def get_totalFollowers(self,obj):
        return obj.followers.count()

    def get_totalFollowings(self,obj):
        return obj.followings.count()

    class Meta:
        model  = ModelUser
        fields = ("username","totalFollowers","totalFollowings","biography","isAnyStory")



