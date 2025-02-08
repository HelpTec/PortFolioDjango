from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
from .models import Master, Persona
from apps.titles.models import Titles



class MasterView(TemplateView):
    name = "home"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datos = Master.objects.first()
        persona = Persona.objects.first()
        context["titulos"] = datos.persona.Titles.all()
        context["datos"] = datos
        return context

    