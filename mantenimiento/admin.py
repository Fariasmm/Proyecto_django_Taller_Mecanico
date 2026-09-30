from django.contrib import admin
from .models import ServicioMantenimiento, OrdenTrabajo

@admin.register(ServicioMantenimiento)
class ServicioMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'costo_mano_obra', 'tiempo_minutos', 'pauta_tecnica')
    search_fields = ('codigo', 'nombre')
    ordering = ('nombre',)

@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ('id', 'patente_moto', 'cliente_nombre', 'servicio', 'repuesto', 'total', 'estado', 'fecha')
    search_fields = ('patente_moto', 'cliente_nombre', 'modelo_moto')
    list_filter = ('estado', 'servicio', 'fecha')
    date_hierarchy = 'fecha'