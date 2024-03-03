from django.shortcuts import render
from rest_framework import viewsets
from portal.models import Producto, Proveedor, SolicitudCompra
from portal.serializer import ProductoSerializer, ProveedorSerializer, SolicitudCompraSerializer

# Create your views here.
class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class SolicitudCompraViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudCompraSerializer
    queryset = SolicitudCompra.objects.all()