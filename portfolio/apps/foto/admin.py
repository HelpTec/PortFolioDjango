from django.contrib import admin

from apps.foto.models import Foto

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ("foto", )