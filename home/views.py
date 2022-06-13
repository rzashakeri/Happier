from django.shortcuts import render, redirect

# from post.forms import UploadPostAttachmentForm, UploadPostForm
from user_management.forms import CustomSigninForm
from user_management.models import User


def home(request):
    if request.user.is_authenticated:
        return redirect("feed")
    else:
        login_form = CustomSigninForm()
        context = {"login_form": login_form}
        return render(request, "home/home_layout.html", context)


def header_component(request, *args, **kwargs):
    """
    checked if user is not logged in set user is None,
    And if we do not do this, we will encounter a render partial error
    """
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    else:
        user = None
    context = {"user": user}
    return render(request, "components/header_component.html", context)
