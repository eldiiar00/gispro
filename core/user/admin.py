from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import *


class UserLocationAdmin(admin.ModelAdmin): 
	list_display = ["user_id", "user_nickname",]
	search_fields = ["user_id", "user_nickname",]
	# list_filter = ["is_active", "is_admin"]

admin.site.register(UserLocation,UserLocationAdmin)


# Register your models here.
