from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@method_decorator(xframe_options_exempt, name="dispatch")
class MasterView(TemplateView):
    name = "home"
    template_name = "home.html"