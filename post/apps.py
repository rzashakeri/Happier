from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "post"

    def ready(self):
        from actstream import registry

        registry.register(self.get_model("Post"))
        registry.register(self.get_model("PostLike"))
        import post.signals
