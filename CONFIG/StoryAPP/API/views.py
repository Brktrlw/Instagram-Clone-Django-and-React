from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import SerializerUserStories,SerializerHomePageStories,SerializerOwnStories,SerializerCreateReadStory
from UserAPP.models import ModelUser
from django.shortcuts import get_object_or_404
from StoryAPP.models import ModelStory,ModelStoryRead
from django.utils import timezone
import datetime
from rest_framework.permissions import IsAuthenticated



datefrom = timezone.now() - datetime.timedelta(days=1)
class UserCurrentStoriesListAPIView(ListAPIView):
    # Kullanıcının adına göre hikayelerini listeler
    serializer_class = SerializerUserStories

    lookup_field = "user__username"
    def get_queryset(self):
        # kullanıcının username'ine göre son 24 saatteki hikayelerini döndürür
        user = get_object_or_404(ModelUser,username=self.kwargs["user__username"])
        return user.get_current_stories()

class HomePageStoriesListAPIView(ListAPIView):
    # Ana sayfada kullanıcının takip ettiği kişilerin hikayelerini listeler
    serializer_class = SerializerHomePageStories
    def get_queryset(self):

        users    = self.request.user.followings.all().values_list('follower_id') # Kullanıcının takip ettiği kişileri listeye alıyoruz
        stories  = ModelStory.objects.filter(user_id__in=users,createdDate__gte=datefrom).order_by("user","-createdDate").distinct("user")
        return stories

class OwnStoriesListAPIView(ListAPIView):
    # Kullanıcı kendi hikayelerini listeler
    serializer_class = SerializerOwnStories
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return ModelStory.objects.filter(user=self.request.user,createdDate__gte=datefrom).order_by("-createdDate")

class StorySeeingCreateAPIView(CreateAPIView):
    # Kullanıcı bir hikayeyi görüntülediğinde okundu olarak eklemek
    serializer_class = SerializerCreateReadStory
    queryset         = ModelStoryRead.objects.all()

    def perform_create(self, serializer):
        story=ModelStory.objects.get(unique_id=serializer.validated_data["story"].get("unique_id"))
        serializer.save(user=self.request.user,story=story)







