from rest_framework.generics import ListAPIView,CreateAPIView
from SavedPostAPP.models import ModelSavedPost
from .serializers import SerializerSavedUserPost,SerializerCreateSavePost
from PostAPP.models import ModelPost
from django.shortcuts import get_object_or_404

class SavedUserPostListAPIView(ListAPIView):
    serializer_class = SerializerSavedUserPost
    def get_queryset(self):
        return ModelSavedPost.objects.filter(user=self.request.user)

class CreateSavedPostAPIView(CreateAPIView):
    queryset          = ModelSavedPost.objects.all()
    serializer_class  = SerializerCreateSavePost

    def perform_create(self, serializer):
        post = get_object_or_404(ModelPost,unique_id=self.kwargs.get("unique_id"))
        serializer.save(user=self.request.user,post=post)








