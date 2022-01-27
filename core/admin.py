from django.contrib import admin
from .models import User, Profile, Channel, Video

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Channel)
admin.site.register(Video)
