from django.contrib import admin

from apps.bio.models import Bio

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = (
        'texto',
        'texto_dos',
        'estudios',
        'trabajos'
    )
