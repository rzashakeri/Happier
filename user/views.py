import json
from actstream.actions import follow, unfollow
from actstream.models import following, followers
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from actstream.actions import follow, unfollow
from .forms import EditPersonalInformationForm, EditProfileForm
from .models import Profile, User

JSON_CONTENT_TYPE = 'application/json'


@verified_email_required
def profile_view(request, username):
    try:
        profiles = Profile.objects.all()[:4]
        # get user profile by username
        profile = Profile.objects.get(user__username__iexact=username)
        user = User.objects.get(username=username)
        user_following = following(user)
        user_followers = followers(user)
        # if user not found raise 404 error
    except ObjectDoesNotExist:
        raise Http404
    # context data
    context = {
        "user": user,
        "profile": profile,
        "profiles": profiles,
        "following": user_following,
        "followers": user_followers,
    }
    return render(request, "user_profile/profile.html", context)


@verified_email_required
def edit_personal_information(request):
    profile_form = EditPersonalInformationForm(instance=request.user)
    # checked request is post?
    if request.method == "POST":
        # send user data to edit profile form
        profile_form = EditPersonalInformationForm(
            request.POST, instance=request.user
        )
        # check user profile form is valid
        if profile_form.is_valid():
            # if user profile is valid, save the form
            profile_form.save()
            # show success message when save user data
            messages.success(request, "Profile saved")
        # put edit profile form with context and send to template
        context = {"profile_form": profile_form}
        # render request and template and context
        return render(
            request, "user_profile/edit_personal_information.html", context
        )
        # pass context
    context = {"profile_form": profile_form}
    return render(request, "user_profile/edit_personal_information.html", context)


@verified_email_required
def edit_profile_view(request):
    profile_form = EditProfileForm(instance=request.user.profile)
    # check request is post?
    if request.method == "POST":
        # send user data to edit profile form
        profile_form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        # check user profile form is valid
        if profile_form.is_valid():
            # if user profile is valid, save the form
            profile_form.save()
            # show success message when save user data
            messages.success(request, "Profile saved")
        # put edit profile form with context and send to template
        context = {"profile_form": profile_form}
        # render request and template and context
        return render(request, "user_profile/edit_profile.html", context)
        # pass context
    context = {"profile_form": profile_form}
    return render(request, "user_profile/edit_profile.html", context)


@verified_email_required
def delete_account_view(request):
    if request.method == "POST":
        data = request.POST.get("delete")
        if data == "yes":
            user = request.user
            logout(request)
            user.delete()
            messages.success(
                request,
                "Your account has been successfully deleted, We hope you will be back soon :)",
            )
            return redirect("home")
        else:
            return redirect("home")
    return render(request, "user_profile/delete_account.html")


@verified_email_required
def follow_request(request, username):
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            current_user_profile = request.user.profile
            if request.user in followers(user):
                unfollow(request.user, user)
                response = {"status": "unfollow"}
                return HttpResponse(
                    json.dumps(response), content_type=JSON_CONTENT_TYPE
                )
            elif profile in current_user_profile.follow_requests.all():
                current_user_profile.follow_requests.remove(profile)
                response = {"status": "cancel_follow_request"}
                return HttpResponse(
                    json.dumps(response), content_type=JSON_CONTENT_TYPE
                )
            else:
                if profile.is_private:
                    current_user_profile.follow_requests.add(profile)
                    response = {"status": "send_follow_request"}
                    return HttpResponse(
                        json.dumps(response), content_type=JSON_CONTENT_TYPE
                    )
                else:
                    follow(request.user, user)
                    response = {"status": "followed"}
                    return HttpResponse(
                        json.dumps(response), content_type=JSON_CONTENT_TYPE
                    )
        except ObjectDoesNotExist:
            response = {"status": "not_found"}
            return HttpResponse(
                json.dumps(response), content_type=JSON_CONTENT_TYPE
            )


def follow_request_accepted(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                user = User.objects.get(username=username)  # We get the current user
                profile = Profile.objects.get(
                    user=user
                )  # We get the current user profile
                current_user_profile = request.user.profile  # We get the logged-in user
                profile.follow_requests.remove(current_user_profile)
                follow(user, request.user)
                profile.save()
                response = {"status": "ok"}
                return HttpResponse(
                    json.dumps(response), content_type=JSON_CONTENT_TYPE
                )
            except ObjectDoesNotExist:
                response = ""
                return HttpResponse(response)
        response = ""
        return HttpResponse(response)
    else:
        return redirect("account_login")


def follow_request_declined(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                profile = Profile.objects.get(user__username__iexact=username)
                current_user_profile = request.user.profile
                current_user_profile.follow_requests.remove(profile)
                current_user_profile.save()
                response = {"status": "ok"}
                return HttpResponse(
                    json.dumps(response), content_type=JSON_CONTENT_TYPE
                )
            except ObjectDoesNotExist:
                response = ""
                return HttpResponse(response)
        response = ""
        return HttpResponse(response)
    else:
        return redirect("account_login")


def follow_request_list(request):
    if request.user.is_authenticated:
        current_user = request.user.profile
        follow_requests = current_user.follow_request_by.all()
        context = {"follow_requests": follow_requests}
        return render(
            request, "activity/follow_request/follow_request_layout.html", context
        )


def followers_list(request, username):
    user = User.objects.get(username=username)
    user_followers = followers(user)
    context = {"followers": user_followers}
    return render(request, "user_profile/followers.html", context)


def followings_list(request, username):
    user = User.objects.get(username=username)
    user_following = following(user)
    context = {"followings": user_following}
    return render(request, "user_profile/following.html", context)
