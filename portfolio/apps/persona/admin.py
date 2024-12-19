from django.contrib import admin

from apps.persona.models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'nombres',
        'apellido',
        'nacimiento',
        'telefono',
        'mail',
        'redes',
        'fotoPerf',
        'bio'
    )