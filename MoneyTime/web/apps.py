from django.apps import AppConfig


class WebConfig(AppConfig):
    name = 'MoneyTime.web'

    def ready(self):
        import MoneyTime.web.signals  # no matter what signal you import,
                                                         # but it nessesary to import all

