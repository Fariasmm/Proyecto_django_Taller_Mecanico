from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('mantenimiento/')),
    path('mantenimiento/', include('mantenimiento.urls')),
    path('repuestos/', include('repuestos.urls')),
]
