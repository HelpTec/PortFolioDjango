from django.contrib import admin

from apps.usuario.models import Usuario

@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_displays = (
        'username',
        'password'
    )