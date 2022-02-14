from rest_framework.generics import ListAPIView
from .serializers import SerializerUserStories,SerializerHomePageStories
from UserAPP.models import ModelUser,ModelFollower
from django.shortcuts import get_object_or_404
from StoryAPP.models import ModelStory
from django.utils import timezone
import datetime
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
        datefrom = timezone.now() - datetime.timedelta(days=1)
        users    = self.request.user.followings.all().values_list('follower_id') # Kullanıcının takip ettiği kişileri listeye alıyoruz
        stories  = ModelStory.objects.filter(user_id__in=users,createdDate__gte=datefrom).order_by("user","-createdDate").distinct("user")
        return stories


