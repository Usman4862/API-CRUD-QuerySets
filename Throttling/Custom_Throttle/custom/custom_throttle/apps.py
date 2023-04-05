from django.apps import AppConfig


class CustomThrottleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_throttle'
