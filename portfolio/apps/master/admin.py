from django.contrib import admin

from apps.master.models import Master

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = (
        'hardcoded',
        'persona'
    )