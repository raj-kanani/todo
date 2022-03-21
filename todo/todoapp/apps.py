from django.apps import AppConfig
from django.core.signals import request_finished


class TodoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'

    def ready(self):
        from . import signals


