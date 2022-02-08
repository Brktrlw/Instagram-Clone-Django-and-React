
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include("PostAPP.API.urls",namespace="post"),name="url_post"),
    path('api/comment/', include("CommentAPP.API.urls", namespace="comment"), name="url_comment"),
    path('api/user/', include("UserAPP.API.urls", namespace="user"), name="url_user"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

