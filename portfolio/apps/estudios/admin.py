from django.contrib import admin

from apps.estudios.models import Estudios

@admin.register(Estudios)
class EstudioAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'establecimiento',
        'urlEstablecimiento',
        'inicio',
        'final',
        'avatarImg'
    )

