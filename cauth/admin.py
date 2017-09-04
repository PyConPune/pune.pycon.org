from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EventUser, UserProfile

admin.site.register(EventUser, UserAdmin)
admin.site.register(UserProfile)
