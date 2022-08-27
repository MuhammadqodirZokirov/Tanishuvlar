from django.contrib import admin
from chat.models import Message, UserProfile, PhotoDuel

admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(PhotoDuel)
