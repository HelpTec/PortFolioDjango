from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
from .models import Master, Persona
from apps.titles.models import Titles
from apps.bio.models import Bio
from apps.estudios.models import Estudios
from apps.redsoc.models import RedSoc
from apps.trabajos.models import Trabajos



class IntroView(TemplateView):
    name = "intro"
    template_name = "intro.html"

class MasterView(TemplateView):
    name = "home"
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datos = Master.objects.first()
        persona = Persona.objects.first()
        bio = Bio.objects.first()

        if persona:
            context["texto_uno"] = bio.textos.first()
            context["texto_dos"] = bio.textos.last()
            context["fotoperf"] = bio.fotoPerf
            context["estudio"] = persona.Estudios.all()
            context["redsoc"] = persona.RedSoc.all()
            context["titulos"] = persona.Titles.all()
            context["trabajos"] = persona.Trabajos.all()
            context["datos"] = datos
            context["estudios"] = persona.Estudios.all()
        return context

    