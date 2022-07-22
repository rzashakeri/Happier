from allauth.account.decorators import verified_email_required
from django.shortcuts import render
from actstream.models import following, followers


@verified_email_required
def feed(request):
    user_followings = following(request.user)
    context = {"followings": user_followings}
    return render(request, "feed/feed.html", context)
