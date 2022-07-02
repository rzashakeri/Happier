import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from comment.forms import CreateCommentModelForm
from comment.models import Comment
from post.models import Post


def create_comment(request, post_id):
    create_comment_form = CreateCommentModelForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            create_comment_form = CreateCommentModelForm(request.POST)
            print(create_comment_form)
            post = Post.objects.get(pk=post_id)
            if create_comment_form.is_valid():
                new_comment = create_comment_form.save(commit=False)
                new_comment.post = post
                new_comment.user = request.user
                new_comment.save()
                comment_count = Comment.objects.filter(post=post).count()
                response = {
                    "result": "OK",
                    "count": comment_count,
                }
                return HttpResponse(
                    json.dumps(response), content_type="application/json"
                )
            else:
                response = {"result": "NOK"}
                return HttpResponse(
                    json.dumps(response), content_type="application/json"
                )
        else:
            return redirect("account_login")
    context = {"create_comment_form": create_comment_form, "post_id": post_id}
    return render(request, "comment/create_comment.html", context)
