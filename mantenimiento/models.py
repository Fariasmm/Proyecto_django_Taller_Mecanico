from django.db import models
from repuestos.models import Repuesto

# Mantenedor 2
class ServicioMantenimiento(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código de Servicio")
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Servicio")
    descripcion = models.TextField(verbose_name="Descripción")
    costo_mano_obra = models.PositiveIntegerField(verbose_name="Mano de Obra ($)")
    tiempo_minutos = models.PositiveIntegerField(verbose_name="Tiempo Estimado (min)")
    # Documento PDF obligatorio por pauta
    pauta_tecnica = models.FileField(upload_to='pautas_pdf/', null=True, blank=True, verbose_name="Pauta Técnica (PDF)")

    def __str__(self):
        return f"{self.nombre} (${self.costo_mano_obra})"

    class Meta:
        verbose_name = "Servicio de Mantenimiento"
        verbose_name_plural = "Servicios de Mantenimiento"


# Transacción obligatoria: Relaciona ambos mantenedores
class OrdenTrabajo(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
        ('Entregado', 'Entregado'),
    ]

    id = models.AutoField(primary_key=True)
    patente_moto = models.CharField(max_length=10, verbose_name="Patente")
    modelo_moto = models.CharField(max_length=100, verbose_name="Modelo Moto")
    cliente_nombre = models.CharField(max_length=150, verbose_name="Nombre Cliente")
    kilometraje = models.PositiveIntegerField(verbose_name="Kilometraje")

    # Claves foráneas obligatorias
    servicio = models.ForeignKey(ServicioMantenimiento, on_delete=models.CASCADE, verbose_name="Servicio")
    repuesto = models.ForeignKey(Repuesto, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Repuesto Utilizado")

    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente', verbose_name="Estado")
    total = models.PositiveIntegerField(default=0, verbose_name="Total ($)")

    def save(self, *args, **kwargs):
        costo_servicio = self.servicio.costo_mano_obra if self.servicio else 0
        costo_repuesto = self.repuesto.precio if self.repuesto else 0
        self.total = costo_servicio + costo_repuesto
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orden #{self.id} - {self.patente_moto}"

    class Meta:
        verbose_name = "Orden de Trabajo"
        verbose_name_plural = "Órdenes de Trabajo"