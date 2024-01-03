from django.apps import AppConfig
from django.contrib import admin


class NotesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"

    def ready(self) -> None:
        from .models import Note

        admin.site.register(Note)
        return super().ready()
