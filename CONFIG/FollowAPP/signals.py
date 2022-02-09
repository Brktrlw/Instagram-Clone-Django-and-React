from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from UserAPP.models import ModelFollower
from NotificationAPP.models import ModelNotification,ModelRequest
from django.db.models import Q

#@receiver(post_save,sender=ModelFollower)
#def whenFollow(sender,instance,*args,**kwargs):
#    follow = ModelFollower.objects.filter(following=instance.following,follower=instance.follower)
#    if follow.count()==2:
#        # takip ederken gelen istek
#        instance.delete()
#        ModelNotification.objects.filter(Q(receiver_user=instance.follower),Q(sender_user=instance.following) | Q(notificationType="2") | Q(notificationType="3")).delete()
#        ModelRequest.objects.filter(receiver_user=instance.follower,sender_user=instance.following).delete()
#
#    elif follow.exists()==1:
#
#        # takip etmiyorken gelen istek
#        if instance.follower.private:
#            #kullanıcının profili gizliyse
#            ModelNotification.objects.create(receiver_user=instance.follower,sender_user=instance.following,notificationType="3")
#            ModelRequest.objects.create(receiver_user=instance.follower,sender_user=instance.following)
#        elif instance.follower.private==False:
#            #kullanıcının profili gizli değilse
#            ModelFollower.objects.create(following=instance.following,follower=instance.follower)
#            ModelNotification.objects.create(receiver_user=instance.follower,sender_user=instance.following,notificationType="2")


