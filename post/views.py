import json

from django.http import HttpResponse
from django.shortcuts import redirect, render

from post.models import PostLike, Post


def post_view(request, slug):
    if request.user.is_authenticated:
        post = Post.objects.get(slug=slug)
        is_liked = PostLike.objects.filter(post=post, user=request.user).exists()
        context = {"post": post, "is_liked": is_liked}
        return render(request, "post/post.html", context)
    else:
        return redirect("account_login")


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
