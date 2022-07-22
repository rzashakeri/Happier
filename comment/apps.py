from django.apps import AppConfig


class CommentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "comment"

    def ready(self):
        from actstream import registry

        registry.register(self.get_model("Comment"))
        import comment.signals
