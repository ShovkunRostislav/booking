from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Booking)
admin.site.register(Flight)
admin.site.register(Airport)