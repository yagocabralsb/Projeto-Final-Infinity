from django.apps import AppConfig


class ControleAcessoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'controle_acesso'

    def ready(self):
        import controle_acesso.signals
