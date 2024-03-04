from django.db import models
from django.core.validators import MinValueValidator

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    contacto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    enlace = models.URLField()
    
    def __str__(self):
        return self.nombre

class SolicitudCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    aprobada = models.BooleanField(default=False)
    
    def calcular_precio_total(self):
        total = sum(item.precio_total() for item in self.items.all())
        self.precio_total = total
        self.save()
    
    def __str__(self):
        return f"Solicitud de compra #{self.id} - Proveedor: {self.proveedor.nombre}"

class ItemCompra(models.Model):
    solicitud = models.ForeignKey(SolicitudCompra, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def precio_total(self):
        return self.cantidad * self.precio_unitario
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.solicitud.calcular_precio_total()  # Update precio_total of SolicitudCompra after saving ItemCompra
