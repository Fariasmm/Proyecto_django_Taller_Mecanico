from rest_framework import viewsets, permissions
from .models import ServicioMantenimiento, OrdenTrabajo
from .serializers import (
    ServicioMantenimientoAdminSerializer,
    ServicioMantenimientoPublicSerializer,
    OrdenTrabajoAdminSerializer,
    OrdenTrabajoPublicSerializer,
)

class ServicioMantenimientoViewSet(viewsets.ModelViewSet):
    """
    CRUD para Mantenedor 2: ServicioMantenimiento.
    El Administrador visualiza 'costo_mano_obra' (dato financiero sensible).
    Los usuarios generales ven el serializador público restringido.
    """
    queryset = ServicioMantenimiento.objects.all()
    serializer_class = ServicioMantenimientoPublicSerializer # Serializer base para Swagger
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        request = getattr(self, 'request', None)
        if request and hasattr(request, 'user') and request.user.is_authenticated and request.user.is_staff:
            return ServicioMantenimientoAdminSerializer
        return ServicioMantenimientoPublicSerializer


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    """
    CRUD para la Transacción: OrdenTrabajo (GET, POST, PUT, DELETE).
    El Administrador visualiza todos los datos del cliente y observaciones.
    Los usuarios generales acceden a la vista operacional restringida.
    """
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoPublicSerializer # Serializer base para Swagger
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        request = getattr(self, 'request', None)
        if request and hasattr(request, 'user') and request.user.is_authenticated and request.user.is_staff:
            return OrdenTrabajoAdminSerializer
        return OrdenTrabajoPublicSerializer