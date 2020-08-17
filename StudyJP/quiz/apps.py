from django.apps import AppConfig
from django.db.models.signals import post_migrate


class QuizConfig(AppConfig):
    name = "quiz"

    def ready(self):
        from .signals import create_default_voca

        post_migrate.connect(create_default_voca, sender=self)
