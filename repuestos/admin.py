from django.contrib import admin
from .models import Repuesto

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'precio', 'stock', 'imagen')
    search_fields = ('codigo', 'nombre', 'categoria')
    list_filter = ('categoria',)
    ordering = ('nombre',)