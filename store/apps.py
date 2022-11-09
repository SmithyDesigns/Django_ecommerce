from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Setting the default auto field to BigAutoField."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
