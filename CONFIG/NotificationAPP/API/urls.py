

from django.urls import path
from .views import NotificationListAPIView



app_name="notification"
urlpatterns = [
    path('list/', NotificationListAPIView.as_view()),
]


