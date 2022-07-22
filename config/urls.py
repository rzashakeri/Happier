"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [  # django admin
    path("admin/", admin.site.urls),
    # local app
    path("", include("feed.urls")),
    path("", include("home.urls")),
    path("", include("user.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth_2fa.urls")),
    path("accounts/", include("allauth.urls")),
    path("post/", include("post.urls")),
    path("comment/", include("comment.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r"", include("user_sessions.urls", "user_sessions")),
    re_path(r"^activity/", include("actstream.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
