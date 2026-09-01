from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_repuestos, name='repuestos_catalogo'),
    path('cotizador/', views.cotizador_repuestos, name='repuestos_cotizador'),
]