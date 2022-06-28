from fluent_comments.forms import (
    CommentFormHelper,
    DefaultCommentForm,
)


class CommentForm(DefaultCommentForm):
    """
    The comment form to use
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = CommentFormHelper()
        self.fields["comment"].widget.attrs[
            "class"
        ] = "pl-3 w-full h-6 bg-slate-100 rounded-lg placeholder:text-slate-600 font-medium pr-20 "
        self.fields["comment"].widget.attrs["placeholder"] = "write a comment..."
        self.fields["comment"].label = ""
        self.fields["comment"].widget.attrs["style"] = "resize: none;"
        self.fields["comment"].widget.attrs["id"] = "comment-form"
