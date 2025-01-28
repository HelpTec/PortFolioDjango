from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

@method_decorator(xframe_options_exempt, name="dispatch")
class EstudiosView(TemplateView):
    name = "estudios"
    template_name = "estudios.html"