# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models

class UserProfileInline(admin.StackedInline):
	model = models.UserProfile
	can_delete = False
	verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.
