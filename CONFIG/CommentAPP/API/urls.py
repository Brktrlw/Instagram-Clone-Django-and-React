
from django.urls import path
from .views import CommentListByPostAPIView
app_name="comment"
urlpatterns = [
    path("list/<str:postunique_id>",CommentListByPostAPIView.as_view(),name="url_commentlist")
]


