from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'user_id', 'img_w', 'img_h')
    list_editable = ('img_w', 'img_h')


admin.site.register(Profile, ProfileAdmin)

