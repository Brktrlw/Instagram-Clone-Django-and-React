from rest_framework.generics import ListAPIView
from SavedPostAPP.models import ModelSavedPost
from .serializers import SerializerSavedUserPost

class SavedUserPostListAPIView(ListAPIView):
    serializer_class = SerializerSavedUserPost
    def get_queryset(self):
        return ModelSavedPost.objects.filter(user=self.request.user)










