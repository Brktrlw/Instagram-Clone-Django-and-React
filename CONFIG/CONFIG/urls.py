
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include("PostAPP.API.urls",namespace="post"),name="url_post"),
    path('api/comment/', include("CommentAPP.API.urls", namespace="comment"), name="url_comment"),
    path('api/user/', include("UserAPP.API.urls", namespace="user"), name="url_user"),
    path('api/savedpost/', include("SavedPostAPP.API.urls", namespace="savedpost"), name="url_savedpost"),
    path('api/story/', include("StoryAPP.API.urls", namespace="stories"), name="url_stories"),
    path('api/like/', include("LikeAPP.API.urls", namespace="likes"), name="url_likes"),
    path('api/notification/', include("NotificationAPP.API.urls", namespace="notification"), name="url_notification"),
    path('api/follow/', include("FollowAPP.API.urls", namespace="follow"), name="url_follow"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

