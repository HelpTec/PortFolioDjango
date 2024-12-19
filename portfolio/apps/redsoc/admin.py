from django.contrib import admin

from apps.redsoc.models import RedSoc

@admin.register(RedSoc)
class RedSocAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'url'
    )