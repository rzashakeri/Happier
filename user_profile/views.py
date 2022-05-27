from allauth.account.decorators import verified_email_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect

from user_profile.forms import EditProfileForm
from user_profile.models import Profile


def profile_view(request, username):
    # We check if the user is logged in?
    if request.user.is_authenticated:
        try:
            profiles = Profile.objects.all()[:4]
            # get user profile by username
            profile = Profile.objects.get(user__username__iexact=username)
        # if user not found raise 404 error
        except ObjectDoesNotExist:
            raise Http404
        # if request methods are POST
        if request.method == 'POST':
            # get current user profile
            current_user_profile = request.user.profile
            # get request data
            data = request.POST
            # get request data with follow name
            action = data.get('follow')
            # if the value of follow is follow
            if action == 'follow':
                # add profile to follows table
                current_user_profile.follows.add(profile)
            # if the value of follow is unfollow
            elif action == 'unfollow':
                # remove profile from follows table
                current_user_profile.follows.remove(profile)
            # save user data
            current_user_profile.save()
        # context data
        context = {
            'profile': profile,
            'profiles': profiles
        }
        return render(request, 'user_profile/profile.html', context)

    # if a user is not login in redirecting to login page
    else:
        return redirect('account_login')


@verified_email_required
def edit_profile_view(request, username):
    # checked user is authenticated
    if request.user.is_authenticated:
        # checked edit profile for current user is which logged in
        if request.user.username == username:
            profile_form = EditProfileForm(instance=request.user)
            if request.method == 'POST':
                profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
                if profile_form.is_valid():
                    profile_form.save()
                context = {
                    'profile_form': profile_form
                }
                return render(request, 'user_profile/edit_profile.html', context)
            # pass context
            context = {
                'profile_form': profile_form
            }
            # return request and template and context
            return render(request, 'user_profile/edit_profile.html', context)
        else:
            """
            If the logged in user is not the same as the user
            who wants to edit the profile raise 404 error
            """
            raise Http404
    # if a user is not authenticated, redirect to login page
    else:
        return redirect(reversed('account_login'))
