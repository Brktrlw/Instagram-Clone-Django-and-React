from rest_framework.generics import CreateAPIView
from PostAPP.models import ModelPost
from .serializers import SerializerPostCreate


class PostCreateAPIView(CreateAPIView):
    queryset         = ModelPost.objects.all()
    serializer_class = SerializerPostCreate

    def perform_create(self, serializer):       # Post kayıt edilirken kullanıcıyı giriş yapmış kullanıcı olarak ayarlıyoruz
        serializer.save(user=self.request.user)
