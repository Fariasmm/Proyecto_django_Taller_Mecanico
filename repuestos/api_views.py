from rest_framework import viewsets, permissions
from .models import Repuesto
from .serializers import RepuestoSerializer

class RepuestoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para el Mantenedor 1: Repuestos (GET, POST, PUT, DELETE).
    Lectura libre; modificaciones requieren autenticación.
    """
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]