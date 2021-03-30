from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 10


# admin.site.register(Project)
