from django.contrib import admin

# Register your models here.
from backEnd.models import Square, UserProfile

admin.site.register(Square)
admin.site.register(UserProfile)