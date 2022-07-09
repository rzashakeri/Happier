import json

from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from user_profile.forms import EditPersonalInformationForm, EditProfileForm
from user_profile.models import Profile


@verified_email_required
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
        # context data
        context = {"profile": profile, "profiles": profiles}
        return render(request, "user_profile/profile.html", context)

    # if a user is not login in redirecting to login page
    else:
        return redirect("account_login")


@verified_email_required
def edit_personal_information(request):
    # checked user is authenticated
    if request.user.is_authenticated:
        # get the edit profile model form
        profile_form = EditPersonalInformationForm(instance=request.user)
        # check request is post?
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
        # return request and template and context
        return render(request, "user_profile/edit_personal_information.html", context)
    # if a user is not authenticated, redirect to login page
    else:
        return redirect(reversed("account_login"))


@verified_email_required
def edit_profile_view(request):
    # checked user is authenticated
    if request.user.is_authenticated:
        # get the edit profile model form
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
        # return request and template and context
        return render(request, "user_profile/edit_profile.html", context)
    # if a user is not authenticated, redirect to login page
    else:
        return redirect(reversed("account_login"))


@verified_email_required
def delete_account_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST.get("delete")
            if data == "yes":
                user = request.user
                user.delete()
                user.save()
                messages.success(
                    request,
                    "Your account has been successfully deleted, We hope you will be back soon :)",
                )
                return redirect("home")
            else:
                return redirect("home")
        return render(request, "user_profile/delete_account.html")
    else:
        return redirect("account_login")


def follow_request(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                profile = Profile.objects.get(user__username__iexact=username)
                current_user_profile = request.user.profile
                if profile in current_user_profile.follows.all():
                    current_user_profile.follows.remove(profile)
                    response = {"status": "unfollow"}
                    return HttpResponse(
                        json.dumps(response), content_type="application/json"
                    )
                elif profile in current_user_profile.follow_requests.all():
                    current_user_profile.follow_requests.remove(profile)
                    response = {"status": "cancel_follow_request"}
                    return HttpResponse(
                        json.dumps(response), content_type="application/json"
                    )
                else:
                    if profile.is_private:
                        current_user_profile.follow_requests.add(profile)
                        response = {"status": "send_follow_request"}
                        return HttpResponse(
                            json.dumps(response), content_type="application/json"
                        )
                    else:
                        current_user_profile.follows.add(profile)
                        response = {"status": "followed"}
                        return HttpResponse(
                            json.dumps(response), content_type="application/json"
                        )
            except ObjectDoesNotExist:
                response = {"status": "not_found"}
                return HttpResponse(
                    json.dumps(response), content_type="application/json"
                )


def follow_request_accepted(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                profile = Profile.objects.get(user__username__iexact=username)
                current_user_profile = request.user.profile

                profile.follow_requests.remove(current_user_profile)
                profile.follows.add(current_user_profile)
                profile.save()

                response = {"status": "ok"}
                return HttpResponse(
                    json.dumps(response), content_type="application/json"
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
                    json.dumps(response), content_type="application/json"
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


def followers(request, username):
    return render(request, "user_profile/followers.html")


def following(request, username):
    return render(request, "user_profile/following.html")
