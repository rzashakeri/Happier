from django.http import Http404
from django.shortcuts import render

from post.forms import UploadPostForm, UploadPostAttachmentForm


def upload_post_view(request):
    # check user is authenticated
    if request.user.is_authenticated:
        # get upload post form
        upload_post_form = UploadPostForm()
        upload_post_attachment_form = UploadPostAttachmentForm()
        # get Post request
        if request.method == "POST":
            # Initialization upload post form
            upload_post_form = UploadPostForm(request.POST)
            upload_post_attachment_form = UploadPostAttachmentForm(
                request.POST, request.FILES
            )
            # Is the reviewed upload form valid?
            if upload_post_form.is_valid():
                # gets model object, and add user data and save
                upload_post = upload_post_form.save(commit=False)
                # get request user id and pass to upload post-form
                upload_post.user = request.user
                # after pass user id form has saved
                upload_post.save()
                post_id = upload_post.id
                if upload_post_attachment_form.data:
                    if upload_post_attachment_form.is_valid():
                        attachment = upload_post_attachment_form.save(commit=False)
                        attachment.post_id = post_id
                        attachment.save()

            # get upload form and pass to context
            context = {
                "upload_post_form": upload_post_form,
                "upload_post_attachment_form": upload_post_attachment_form,
            }
            # return request and template with context when request method is post
            return render(request, "post/upload_post.html", context)
        # return request and template with context when request method is get
        context = {
            "upload_post_form": upload_post_form,
            "upload_post_attachment_form": upload_post_attachment_form,
        }
        return render(request, "post/upload_post.html", context)
    else:
        # if a user isn't authenticated, show not found(404) page
        raise Http404
