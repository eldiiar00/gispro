from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class PartnersAdmin(SummernoteModelAdmin): 
	list_display = ["title",]
	search_fields = ["title"]
	list_filter = ["choosen"]
	summernote_fields = ('description',)


admin.site.register(Partners, PartnersAdmin)
admin.site.register(Services)
