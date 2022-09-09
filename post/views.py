import json
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from post.forms import UploadPostForm
from post.models import PostLike, Post
from utils.text_parser import extract_hashtags
from django import forms


@verified_email_required
def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    is_liked = PostLike.objects.filter(post=post, user=request.user).exists()
    context = {"post": post, "is_liked": is_liked}
    return render(request, "post/post.html", context)


@verified_email_required
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


@verified_email_required
def create_new_post_view(request):
    upload_post_form = UploadPostForm()
    if request.method == "POST":
        upload_post_form = UploadPostForm(request.POST, request.FILES)
        if upload_post_form.is_valid():
            new_post = upload_post_form.save(commit=False)
            new_post.user_id = request.user.id
            new_post.save()
            messages.success(request, "Your post has been published")
            return redirect("feed")
        else:
            context = {"upload_post_form": upload_post_form}
            return render(request, "post/create_new_post.html", context)

    context = {"upload_post_form": upload_post_form}
    return render(request, "post/create_new_post.html", context)
