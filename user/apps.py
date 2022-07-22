from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
    verbose_name = "user"

    def ready(self):
        from actstream import registry

        registry.register(self.get_model("User"))
        import user.signals
