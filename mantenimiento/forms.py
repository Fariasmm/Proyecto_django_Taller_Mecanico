from django import forms
from .models import OrdenTrabajo, ServicioMantenimiento

class ServicioMantenimientoForm(forms.ModelForm):
    class Meta:
        model = ServicioMantenimiento
        fields = ['codigo', 'nombre', 'descripcion', 'costo_mano_obra', 'tiempo_minutos', 'pauta_tecnica']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: SRV-01'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del servicio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada'}),
            'costo_mano_obra': forms.NumberInput(attrs={'class': 'form-control'}),
            'tiempo_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
            'pauta_tecnica': forms.FileInput(attrs={'class': 'form-control'}),
        }

class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = ['patente_moto', 'modelo_moto', 'cliente_nombre', 'kilometraje', 'servicio', 'repuesto', 'estado']
        widgets = {
            'patente_moto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: AB123'}),
            'modelo_moto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Yamaha FZ 150'}),
            'cliente_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del cliente'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Km actual'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'repuesto': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }