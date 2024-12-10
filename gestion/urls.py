from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctores/', views.doctores, name='doctores'),
    path('pacientes/', views.pacientes, name='pacientes'), 
]