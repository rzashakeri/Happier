from django.shortcuts import render
from actstream.models import following, followers
from actstream.models import user_stream, actor_stream


def activity(request):
    user_followers = followers(request.user)
    user_following = following(request.user)
    activities = user_stream(request.user, with_user_activity=True)
    my_activities = actor_stream(request.user)

    context = {
        "followings": user_following,
        "followers": user_followers,
        "activities": activities,
        "my_activities": my_activities,
    }
    return render(request, "activity/activity_layout.html", context)
