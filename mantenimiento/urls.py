from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_mantenimiento, name='mantenimiento_inicio'),
    path('servicios/', views.lista_servicios, name='mantenimiento_servicios'),
    path('servicios/nuevo/', views.servicio_crear, name='servicio_crear'),
    path('servicios/editar/<int:id>/', views.servicio_editar, name='servicio_editar'),
    path('servicios/eliminar/<int:id>/', views.servicio_eliminar, name='servicio_eliminar'),
    
    # Rutas de la Transacción
    path('ordenes/', views.ordenes_listar, name='ordenes_listar'),
    path('ordenes/nueva/', views.orden_crear, name='orden_crear'),
    path('ordenes/editar/<int:id>/', views.orden_editar, name='orden_editar'),       # <-- NUEVA RUTA
    path('ordenes/eliminar/<int:id>/', views.orden_eliminar, name='orden_eliminar'),
]