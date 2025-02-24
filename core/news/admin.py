from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class NewsAdmin(SummernoteModelAdmin): 
	search_fields = ["title", "summary",]
	list_display = ["title", "created_at",]
	list_filter = ["created_at"]
	summernote_fields = ('content',)

admin.site.register(News,NewsAdmin)
