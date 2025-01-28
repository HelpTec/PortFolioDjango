from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

@method_decorator(xframe_options_exempt, name="dispatch")
class RedsocView(TemplateView):
    name = "redsoc"
    template_name = "redsoc.html"