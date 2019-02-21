from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):  # some func for import
        import users.signals
