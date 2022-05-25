from django.shortcuts import render

from user_management.forms import CustomSigninForm


def home(request):
    login_form = CustomSigninForm()
    context = {
        'login_form': login_form
    }
    return render(request, 'home/home_layout.html', context)
