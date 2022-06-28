import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_comments.models import Comment

from post.forms import CommentForm
from post.models import Like, Post


def post_view(request, slug):
    if request.user.is_authenticated:
        post = Post.objects.get(slug=slug)
        create_comment_form = CommentForm(target_object=post)
        context = {"post": post, "create_comment_form": create_comment_form}
        return render(request, "post/post.html", context)
    else:
        return redirect("account_login")


def like_view(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        print(post_id)
        liked = Like.objects.filter(user_id=request.user.id, post=post).first()
        if liked:
            Like.delete(liked)
            like_count = Like.objects.filter(post=post).count()
            response_data = {"result": "unliked", "like_count": like_count}
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )

        else:
            new_like = Like(user=request.user, post=post)
            new_like.save()
            like_count = Like.objects.filter(post=post).count()
            response_data = {"result": "liked", "like_count": like_count}
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )


def create_comment_view(request, post_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST)
            create_comment_form = CommentForm(request.POST)
            post = Post.objects.get(pk=post_id)
            if create_comment_form.is_valid():
                form = create_comment_form.save(commit=False)
                form.user = request.user
                form.post = post
                form.save()
                comment_count = Comment.objects.filter(post=post).count()
                response = {"result": "OK", "comment_count": comment_count}
                return HttpResponse(
                    json.dumps(response), content_type="application/json"
                )
            else:
                response = {"result": "NOK", "error": "form is not valid !"}
                return HttpResponse(
                    json.dumps(response), content_type="application/json"
                )

    else:
        return redirect("account_login")
