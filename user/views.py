import json
import os
from abc import ABC

from actstream.actions import follow, unfollow
from actstream.models import following, followers
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage, DefaultStorage
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from actstream.actions import follow, unfollow

from config import settings
import user.forms as form
from user.models import Profile, User
from formtools.wizard.views import SessionWizardView, WizardView

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
    return render(request, "user/profile.html", context)


@verified_email_required
def edit_personal_information(request):
    profile_form = form.EditPersonalInformationForm(instance=request.user)
    # checked request is post?
    if request.method == "POST":
        # send user data to edit profile form
        profile_form = form.EditPersonalInformationForm(
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
            request, "user/edit_personal_information.html", context
        )
        # pass context
    context = {"profile_form": profile_form}
    return render(request, "user/edit_personal_information.html", context)


@verified_email_required
def edit_profile_view(request):
    profile_form = form.EditProfileForm(instance=request.user.profile)
    # check request is post?
    if request.method == "POST":
        # send user data to edit profile form
        profile_form = form.EditProfileForm(
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
        return render(request, "user/edit_profile.html", context)
        # pass context
    context = {"profile_form": profile_form}
    return render(request, "user/edit_profile.html", context)


def delete_profile_image(request):
    if request.method == "POST":
        profile_image = request.user.profile.profile_image
        profile_image.delete()
        response = {"status": "ok"}
        return HttpResponse(json.dumps(response), content_type=JSON_CONTENT_TYPE)
    else:
        response = ""
        return HttpResponse(response)


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
    return render(request, "user/delete_account.html")


@verified_email_required
def follow_request(request, username):
    if request.method == "POST":
        try:
            user_whose_page_is_currently_being_viewed = User.objects.get(username=username)
            profile_whose_page_is_currently_being_viewed = Profile.objects.get(user=user_whose_page_is_currently_being_viewed)
            authenticated_user_profile = request.user.profile
            if request.user in followers(user_whose_page_is_currently_being_viewed):
                unfollow(request.user, user_whose_page_is_currently_being_viewed)
                response = {"status": "unfollow"}
                return HttpResponse(
                    json.dumps(response), content_type=JSON_CONTENT_TYPE
                )
            elif profile_whose_page_is_currently_being_viewed in authenticated_user_profile.follow_requests.all():
                authenticated_user_profile.follow_requests.remove(profile_whose_page_is_currently_being_viewed)
                response = {"status": "cancel_follow_request"}
                return HttpResponse(
                    json.dumps(response), content_type=JSON_CONTENT_TYPE
                )
            else:
                if profile_whose_page_is_currently_being_viewed.is_private:
                    authenticated_user_profile.follow_requests.add(profile_whose_page_is_currently_being_viewed)
                    response = {"status": "send_follow_request"}
                    return HttpResponse(
                        json.dumps(response), content_type=JSON_CONTENT_TYPE
                    )
                else:
                    follow(request.user, user_whose_page_is_currently_being_viewed)
                    response = {"status": "followed"}
                    return HttpResponse(
                        json.dumps(response), content_type=JSON_CONTENT_TYPE
                    )
        except ObjectDoesNotExist:
            response = {"status": "not_found"}
            return HttpResponse(
                json.dumps(response), content_type=JSON_CONTENT_TYPE
            )


@verified_email_required
def follow_request_accepted(request, username):
    if request.method == "POST":
        try:
            user_whose_page_is_currently_being_viewed = User.objects.get(username=username)  # We get the current user
            profile_whose_page_is_currently_being_viewed = Profile.objects.get(
                user=user_whose_page_is_currently_being_viewed
            )  # We get the current user profile
            authenticated_user_profile = request.user.profile  # We get the logged-in user
            profile_whose_page_is_currently_being_viewed.follow_requests.remove(authenticated_user_profile)
            follow(user_whose_page_is_currently_being_viewed, request.user)
            profile_whose_page_is_currently_being_viewed.save()
            response = {"status": "ok"}
            return HttpResponse(
                json.dumps(response), content_type=JSON_CONTENT_TYPE
            )
        except ObjectDoesNotExist:
            response = ""
            return HttpResponse(response)
    response = ""
    return HttpResponse(response)


@verified_email_required
def follow_request_declined(request, username):
    if request.method == "POST":
        try:
            profile_whose_page_is_currently_being_viewed = Profile.objects.get(user__username__iexact=username)
            authenticated_user_profile = request.user.profile
            authenticated_user_profile.follow_requests.remove(profile_whose_page_is_currently_being_viewed)
            authenticated_user_profile.save()
            response = {"status": "ok"}
            return HttpResponse(
                json.dumps(response), content_type=JSON_CONTENT_TYPE
            )
        except ObjectDoesNotExist:
            response = ""
            return HttpResponse(response)
    response = ""
    return HttpResponse(response)


@verified_email_required
def follow_request_list(request):
    current_user = request.user.profile
    follow_requests = current_user.follow_request_by.all()
    context = {"follow_requests": follow_requests}
    return render(
        request, "activity/follow_request/follow_request_layout.html", context
    )


@verified_email_required
def followers_list(request, username):
    user = User.objects.get(username=username)
    user_followers = followers(user)
    context = {"followers": user_followers}
    return render(request, "user/followers.html", context)


@verified_email_required
def followings_list(request, username):
    user = User.objects.get(username=username)
    user_following = following(user)
    context = {"followings": user_following}
    return render(request, "user/following.html", context)


def remove_welcome_message(request):
    if request.method == "POST":
        profile = request.user.profile
        profile.show_welcome_message = False
        profile.save()
        response = {"status": "ok"}
        return HttpResponse(json.dumps(response), content_type="application/json")


class UserWizard(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'temp'))

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        first_name = form_data[0]["first_name"]
        last_name = form_data[0]["last_name"]
        biography = form_data[1]["biography"]
        birthday = form_data[2]["birthday"]
        job = form_data[3]["job"]
        profile_image = form_data[4]["profile_image"]

        current_user = self.request.user
        user = User.objects.get(pk=current_user.pk)
        if first_name is not None:
            user.first_name = first_name
            user.save()

        if last_name is not None:
            user.last_name = last_name
            user.save()

        profile = Profile.objects.get(user=user)
        if biography is not None:
            profile.biography = biography
            profile.save()

        if birthday is not None:
            profile.birthday = birthday
            profile.save()

        if job is not None:
            profile.job = job
            profile.save()

        if profile_image is not None:
            profile.profile_image = profile_image
            profile.save()

        remove_welcome_message(self.request)

        response = {"status": "ok"}
        return HttpResponse(json.dumps(response), content_type="application/json")
