from django import forms
from docutils.nodes import caption
from file_validator.django import FileValidator
from ckeditor.widgets import CKEditorWidget
from post.models import Post


class UploadPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "file"]
        widgets = {
            "caption": CKEditorWidget(
                config_name="default",
                extra_plugins=[
                    "emoji",
                    "textmatch",
                    "textwatcher",
                    "codesnippet",
                    "wordcount",
                    "justify",
                ],
                # CKEDITOR.plugins.addExternal(...)
                external_plugin_resources=[
                    (
                        "emoji",
                        "/static/ckeditor/ckeditor/plugins/emoji/",
                        "plugin.js",
                    ),
                    (
                        "textmatch",
                        "/static/ckeditor/ckeditor/plugins/textmatch/",
                        "plugin.js",
                    ),
                    (
                        "textwatcher",
                        "/static/ckeditor/ckeditor/plugins/textwatcher/",
                        "plugin.js",
                    ),
                    (
                        "autocomplete",
                        "/static/ckeditor/ckeditor/plugins/autocomplete/",
                        "plugin.js",
                    ),
                    (
                        "codesnippet",
                        "/static/ckeditor/ckeditor/plugins/codesnippet/",
                        "plugin.js",
                    ),
                    (
                        "wordcount",
                        "/static/ckeditor/ckeditor/plugins/wordcount/",
                        "plugin.js",
                    ),
                    (
                        "justify",
                        "/static/ckeditor/ckeditor/plugins/justify/",
                        "plugin.js",
                    ),
                ],
            ),
            "file": forms.FileInput(
                attrs={
                    "accept": "image/png, video/mp4, audio/mpeg",
                    "onchange": "loadFile(event)",
                }
            ),
        }


# Upload Post-Form In Seperated Form


class UploadMediaForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/png, video/mp4, audio/mpeg",
                "onchange": "loadFile(event)",
            }
        ),
        required=False
    )


class UploadCaptionForm(forms.Form):
    caption = forms.CharField(
        widget=CKEditorWidget(
            config_name="default",
            extra_plugins=[
                "emoji",
                "textmatch",
                "textwatcher",
                "codesnippet",
                "wordcount",
                "justify",
            ],
            external_plugin_resources=[
                (
                    "emoji",
                    "/static/ckeditor/ckeditor/plugins/emoji/",
                    "plugin.js",
                ),
                (
                    "textmatch",
                    "/static/ckeditor/ckeditor/plugins/textmatch/",
                    "plugin.js",
                ),
                (
                    "textwatcher",
                    "/static/ckeditor/ckeditor/plugins/textwatcher/",
                    "plugin.js",
                ),
                (
                    "autocomplete",
                    "/static/ckeditor/ckeditor/plugins/autocomplete/",
                    "plugin.js",
                ),
                (
                    "codesnippet",
                    "/static/ckeditor/ckeditor/plugins/codesnippet/",
                    "plugin.js",
                ),
                (
                    "wordcount",
                    "/static/ckeditor/ckeditor/plugins/wordcount/",
                    "plugin.js",
                ),
                ("justify", "/static/ckeditor/ckeditor/plugins/justify/", "plugin.js"),
            ],
        )
    )
