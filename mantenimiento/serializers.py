from rest_framework import serializers
from .models import ServicioMantenimiento, OrdenTrabajo

# Mantenedor 2: ServicioMantenimiento
class ServicioMantenimientoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioMantenimiento
        fields = '__all__'

class ServicioMantenimientoPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioMantenimiento
        fields = ['id', 'codigo', 'nombre', 'descripcion', 'tiempo_minutos', 'pauta_tecnica']

# Transacción: OrdenTrabajo
class OrdenTrabajoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'

class OrdenTrabajoPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        # Se reemplaza 'numero_orden' por 'id'
        fields = ['id', 'patente_moto', 'servicio', 'repuesto', 'estado', 'fecha']