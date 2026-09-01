from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_mantenimiento, name='mantenimiento_inicio'),

    path('servicios/', views.lista_servicios, name='mantenimiento_servicios'),
]