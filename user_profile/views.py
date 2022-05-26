from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect

from user_management.models import User


def profile_view(request, username):
    # We check if the user is logged in?
    if request.user.is_authenticated:
        try:
            # get user by username
            current_user = User.objects.get(username__iexact=username)
        # if user not found raise 404 error
        except ObjectDoesNotExist:
            raise Http404

        context = {
            'user': current_user
        }
        return render(request, 'user_profile/profile.html', context)
    # if a user is not login in redirecting to login page
    else:
        return redirect('account_login')
