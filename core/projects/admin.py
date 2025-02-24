from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class ProjectsAdmin(SummernoteModelAdmin): 
	list_display = ["title", "period","created_at",]
	search_fields = ["title", "summary",]
	list_filter = ["choosen", "created_at"]
	summernote_fields = ('content',)

admin.site.register(Projects,ProjectsAdmin)
