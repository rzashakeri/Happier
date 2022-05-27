from django.shortcuts import render

from user_management.forms import CustomSigninForm
from user_management.models import User


def home(request):
    login_form = CustomSigninForm()
    context = {
        'login_form': login_form
    }
    return render(request, 'home/home_layout.html', context)


def header_component(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'components/header_component.html', context)
