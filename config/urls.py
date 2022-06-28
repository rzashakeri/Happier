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
    path("", include("user_management.urls")),
    path("", include("feed.urls")),
    path("", include("home.urls")),
    # user_management app
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth_2fa.urls")),
    path("accounts/", include("allauth.urls")),
    # user profile app
    path("", include("user_profile.urls")),
    path("post/", include("post.urls")),
    re_path(r"", include("user_sessions.urls", "user_sessions")),
    re_path(r"^comments/", include("django_comments.urls")),
    re_path(r"^blog/comments/", include("fluent_comments.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
