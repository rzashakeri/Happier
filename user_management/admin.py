from django.contrib import admin

from .models import User


# class for show user data in admin
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_joined', 'is_active']
    list_filter = ['date_joined', 'last_login']
    list_editable = ['email', 'is_active']


admin.site.register(User, UserAdmin)
