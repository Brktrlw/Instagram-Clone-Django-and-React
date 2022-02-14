from rest_framework.generics import ListAPIView
from .serializers import SerializerUserStories,SerializerHomePageStories
from UserAPP.models import ModelUser,ModelFollower
from django.shortcuts import get_object_or_404
from StoryAPP.models import ModelStory

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
        users=self.request.user.followings.all().values_list('follower_id') # Kullanıcının takip ettiği kişileri listeye alıyoruz
        return ModelStory.objects.filter(user_id__in=users)



