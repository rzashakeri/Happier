from django.contrib import admin

from .models import Profile
from .models import User


class ProfileInline(admin.StackedInline):
    model = Profile


# class for show user data in admin
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "date_joined", "is_active"]
    list_filter = ["date_joined", "last_login"]
    list_editable = ["is_active"]
    inlines = [ProfileInline]


admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]


admin.site.register(Profile, ProfileAdmin)
