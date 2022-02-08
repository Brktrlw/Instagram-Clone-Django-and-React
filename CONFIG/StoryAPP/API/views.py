from rest_framework.generics import ListAPIView
from .serializers import SerializerUserStories
from UserAPP.models import ModelUser
from django.shortcuts import get_object_or_404

class UserCurrentStoriesListAPIView(ListAPIView):
    # Kullanıcının adına göre hikayelerini listeler
    serializer_class = SerializerUserStories

    lookup_field = "user__username"
    def get_queryset(self):
        # kullanıcının username'ine göre son 24 saatteki hikayelerini döndürür
        user = get_object_or_404(ModelUser,username=self.kwargs["user__username"])
        return user.get_current_stories()




