from django.shortcuts import render

from user_management.forms import CustomSigninForm
from user_management.models import User


def home(request):
    login_form = CustomSigninForm()
    if request.user.is_authenticated:
        return render(request, "feed/feed.html")
    else:
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
