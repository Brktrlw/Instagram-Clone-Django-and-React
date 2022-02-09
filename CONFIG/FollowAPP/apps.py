from django.apps import AppConfig


class FollowappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FollowAPP'

    def ready(self):
        import FollowAPP.signals
