from django.shortcuts import render
from rest_framework import viewsets, status
from portal.models import ItemCompra, Producto, Proveedor, SolicitudCompra
from portal.serializer import ItemCompraSerializer, ProductoSerializer, ProveedorSerializer, SolicitudCompraSerializer
from rest_framework.response import Response

# Create your views here.
class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def create(self, request, *args, **kwargs):
        # Verificar si la solicitud contiene una lista de productos
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SolicitudCompraViewSet(viewsets.ModelViewSet):
    queryset = SolicitudCompra.objects.prefetch_related('items') 
    serializer_class = SolicitudCompraSerializer


class ItemCompraViewSet(viewsets.ModelViewSet):
    serializer_class = ItemCompraSerializer
    queryset = ItemCompra.objects.all()

    def create(self, request, *args, **kwargs):
        # Verificar si la solicitud contiene una lista de productos
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)