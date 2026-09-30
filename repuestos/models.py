from django.db import models

class Repuesto(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    categoria = models.CharField(max_length=100, verbose_name="Categoría")
    precio = models.PositiveIntegerField(verbose_name="Precio ($)")
    stock = models.PositiveIntegerField(verbose_name="Stock disponible")
    # Imagen obligatoria por pauta
    imagen = models.ImageField(upload_to='repuestos/', null=True, blank=True, verbose_name="Foto del Repuesto")

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

    class Meta:
        verbose_name = "Repuesto"
        verbose_name_plural = "Repuestos"