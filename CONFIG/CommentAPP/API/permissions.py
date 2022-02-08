from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from UserAPP.models import ModelFollower
from PostAPP.models import ModelPost

class IsFollowing(BasePermission):      # Kullanıcı takip ediyorsa postların yorumlarını gösterir,eğer takip etmiyorsa VE gizli hesapsa göstermez.
    message="Kullanıcının profili gizli"
    def has_permission(self, request, view):
        auth_user   = request.user
        post        = get_object_or_404(ModelPost,unique_id=view.kwargs.get("postunique_id"))
        target_user = post.user

        if auth_user==target_user:
            return True
        isFollowing = ModelFollower.objects.filter(follower=target_user, following=auth_user).exists()
        if target_user.private==True and isFollowing==False:
            return False
        return True

class IsOwner(BasePermission):
    message = "You must be the owner this object for any process"

    def has_object_permission(self, request, view, obj):
        print(obj.post.user)
        return (obj.post.user == request.user) or (obj.user == request.user)
        # silinecek yorumun postunun sahibi ile silmek isteyen kullanıcı aynı ise True döndürür
        # OR
        # silinecek yorumun sahibi ,silme isteğini atan kullanıcı ise True döndürür

