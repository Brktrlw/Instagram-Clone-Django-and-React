from rest_framework.generics import ListAPIView
from StoryAPP.models import ModelStory
from .serializers import SerializerUserStories
import datetime

class UserCurrentStoriesListAPIView(ListAPIView):
    # Kullanıcının hikayelerini gösterir
    serializer_class = SerializerUserStories

    lookup_field = "user__username"
    def get_queryset(self):
        # son 24 saatteki hikayeleri döndürür
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        return ModelStory.objects.filter(user__username=self.kwargs["user__username"],createdDate__gte=date_from)




