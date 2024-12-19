from django.contrib import admin

from apps.trabajos.models import Trabajos

@admin.register(Trabajos)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = (
        'ocupacion',
        'empresa',
        'urlEmpresa',
        'inicio',
        'final',
        'avatarImg'
    )
