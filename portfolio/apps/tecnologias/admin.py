from django.contrib import admin
from apps.tecnologias.models import Tecnologias

@admin.register(Tecnologias)
class EstudioAdmin(admin.ModelAdmin):
    list_display = (
        'Persona',
        'avatarImg',
        'nombre',
        'nivel'
    )
