
from django.urls import path
from .views import CommentListByPostAPIView,CreateCommentAPIView,DeleteCommentAPIView

app_name="comment"
urlpatterns = [
    path("list/<str:postunique_id>",CommentListByPostAPIView.as_view(),name="url_commentlist"),   # Herhangi bir postun yorumlarını çeker
    path("create/<str:postunique_id>",CreateCommentAPIView.as_view(),name="url_commentcreate"),   # Yorum yapma işlemi
    path("delete/<unique_id>", DeleteCommentAPIView.as_view(), name="url_commentdelete"),         # Yorum silme
]


