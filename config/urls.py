from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# DRF Router
from rest_framework.routers import DefaultRouter

# API ViewSets de tus aplicaciones
from repuestos.api_views import RepuestoViewSet
from mantenimiento.api_views import ServicioMantenimientoViewSet, OrdenTrabajoViewSet

# Endpoints SimpleJWT para autenticación de tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger / OpenAPI (drf-spectacular)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# Configuración y registro de rutas de la API en el router
router = DefaultRouter()
router.register(r'repuestos', RepuestoViewSet, basename='api-repuestos')
router.register(r'servicios', ServicioMantenimientoViewSet, basename='api-servicios')
router.register(r'ordenes-trabajo', OrdenTrabajoViewSet, basename='api-ordenes-trabajo')

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Rutas Web Originales (Evaluación 2)
    path('', lambda request: redirect('mantenimiento_inicio')),
    path('mantenimiento/', include('mantenimiento.urls')),
    path('repuestos/', include('repuestos.urls')),
    
    # Rutas de Autenticación Requeridas por Pauta Web
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # ==========================================
    # NUEVAS RUTAS API RESTFUL (Evaluación 3)
    # ==========================================
    
    # 1. Endpoints RESTful de los recursos (CRUD completo)
    path('api/', include(router.urls)),

    # 2. Autenticación con JWT (Obtención y Renovación de Tokens)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 3. Documentación OpenAPI y Swagger UI interactiva
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Servir archivos media (imágenes y PDFs) durante desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)