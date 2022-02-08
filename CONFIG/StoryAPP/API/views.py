from rest_framework.generics import ListAPIView
from StoryAPP.models import ModelStory
from .serializers import SerializerUserStories

class UserStoriesListAPIView(ListAPIView):
    serializer_class = SerializerUserStories

    lookup_field = "user__username"
    def get_queryset(self):
        return ModelStory.objects.filter(user__username=self.kwargs["user__username"])




