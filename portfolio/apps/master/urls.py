from django.urls import path
from . import views

urlpatterns = [
    path('', views.IntroView.as_view(), name='intro'),
    path('home', views.MasterView.as_view(), name='master')
]