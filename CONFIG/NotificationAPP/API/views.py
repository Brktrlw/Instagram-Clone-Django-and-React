from rest_framework.generics import ListAPIView
from .serializers import SerializerListNotification


class NotificationListAPIView(ListAPIView):
    # Kullanıcının tüm bildirimlerini listeler
    serializer_class = SerializerListNotification

    def get_queryset(self):
        return self.request.user.notifications.all()


