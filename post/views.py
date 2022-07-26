import json

from allauth.account.decorators import verified_email_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from post.models import PostLike, Post


@verified_email_required
def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    is_liked = PostLike.objects.filter(post=post, user=request.user).exists()
    context = {"post": post, "is_liked": is_liked}
    return render(request, "post/post.html", context)


def like_view(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        print(post_id)
        liked = PostLike.objects.filter(user_id=request.user.id, post=post).first()
        if liked:
            PostLike.delete(liked)
            like_count = PostLike.objects.filter(post=post).count()
            response_data = {"result": "unliked", "like_count": like_count}
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )
        else:
            new_like = PostLike(user=request.user, post=post)
            new_like.save()
            like_count = PostLike.objects.filter(post=post).count()
            response_data = {"result": "liked", "like_count": like_count}
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )


@verified_email_required
def show_post_view(request, slug):
    post = Post.objects.get(slug=slug)
    context = {"post": post}
    return render(request, "post/post_layout.html", context)
