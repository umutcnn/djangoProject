from django.contrib import admin

from home.models import Setting, UserProfile

admin.site.register(Setting)
admin.site.register(UserProfile)