from django.apps import AppConfig


class WebapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapi'

    def ready(self):
        import webapi.signals