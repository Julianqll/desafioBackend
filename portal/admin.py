from django.contrib import admin

from portal.models import ItemCompra, Producto, Proveedor, SolicitudCompra

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(SolicitudCompra)
admin.site.register(ItemCompra)