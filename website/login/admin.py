from django.contrib import admin

# Register your models here.

from login.models import users

admin.site.register(users)
