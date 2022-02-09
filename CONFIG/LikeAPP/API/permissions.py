
from rest_framework.permissions import BasePermission
from UserAPP.models import ModelUser,ModelFollower
from django.shortcuts import get_object_or_404
from PostAPP.models import ModelPost
from CommentAPP.models import ModelComment

class IsFollowingOrOwnPost(BasePermission):
    # Kullanıcı takip ediyorsa postları gösterir,eğer takip etmiyorsa VE gizli hesapsa göstermez.
    message="Kullanıcının profili gizli"
    def has_permission(self, request, view):
        auth_user   = request.user
        target_user = get_object_or_404(ModelPost,unique_id=view.kwargs.get("unique_id")).user
        if auth_user==target_user: # eğer kendi postunun beğenilerine bakıyorsa True döner
            return True
        isFollowing = ModelFollower.objects.filter(follower=target_user, following=auth_user).exists()
        if target_user.private==True and isFollowing==False:
            return False
        return True

class IsFollowingOrOwnComment(BasePermission):
    # Kullanıcı takip ediyorsa yorum gösterir,eğer takip etmiyorsa VE gizli hesapsa göstermez.
    message="Kullanıcının profili gizli"
    def has_permission(self, request, view):
        auth_user   = request.user
        target_user = get_object_or_404(ModelComment,unique_id=view.kwargs.get("unique_id")).post.user
        if auth_user==target_user: # eğer kendi postunun beğenilerine bakıyorsa True döner
            return True
        isFollowing = ModelFollower.objects.filter(follower=target_user, following=auth_user).exists()
        if target_user.private==True and isFollowing==False:
            return False
        return True




