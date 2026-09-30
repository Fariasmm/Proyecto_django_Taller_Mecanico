from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo_repuestos, name='repuestos_catalogo'),
    path('nuevo/', views.repuesto_crear, name='repuesto_crear'),
    path('editar/<int:id>/', views.repuesto_editar, name='repuesto_editar'),
    path('eliminar/<int:id>/', views.repuesto_eliminar, name='repuesto_eliminar'),
    path('cotizador/', views.cotizador_repuestos, name='repuestos_cotizador'),
]