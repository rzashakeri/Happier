from django.shortcuts import render, redirect

from user_management.models import User


def profile_view(request, username):
    if request.user.is_authenticated:
        current_user = User.objects.get(username__iexact=username)
        context = {
            'user': current_user
        }
        return render(request, 'user_profile/profile.html', context)
    else:
        return redirect('account_login')
