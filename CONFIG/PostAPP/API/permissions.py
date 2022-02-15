from rest_framework.permissions import BasePermission
from UserAPP.models import ModelUser,ModelFollower
from django.shortcuts import get_object_or_404

class IsOwner(BasePermission):
    message = "You must be the owner this object for any process"

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user)

class IsFollowing(BasePermission):
    # Kullanıcı takip ediyorsa postları gösterir,eğer takip etmiyorsa VE gizli hesapsa göstermez.
    message="Kullanıcının profili gizli"
    def has_permission(self, request, view):
        auth_user   = request.user
        target_user = get_object_or_404(ModelUser,username=view.kwargs.get("user__username"))
        if auth_user==target_user:
            return True
        isFollowing = ModelFollower.objects.filter(follower=target_user, following=auth_user).exists()
        if target_user.private==True and isFollowing==False:
            return False
        return True

