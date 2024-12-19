from django.contrib import admin

from apps.titles.models import Titles

@admin.register(Titles)
class postAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
