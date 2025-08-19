from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ecommerce.apps.accounts'

    def ready(self):
        from Ecommerce.apps.accounts import signals