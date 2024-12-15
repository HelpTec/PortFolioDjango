from django.urls import path
from . import views

urlpatterns = [
    path('', views.MasterView.as_view(), name='master')
]