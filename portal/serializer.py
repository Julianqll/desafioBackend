from rest_framework import serializers
from .models import Proveedor, Producto, SolicitudCompra, ItemCompra
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'password', 'groups']


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ItemCompraSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(write_only=True)  # Establecer write_only=True

    class Meta:
        model = ItemCompra
        fields = '__all__'

    def create(self, validated_data):
        producto_data = validated_data.pop('producto')
        producto, created = Producto.objects.get_or_create(**producto_data)
        item_compra = ItemCompra.objects.create(producto=producto, **validated_data)
        return item_compra
    def to_representation(self, instance):
        # Sobreescribir este método para incluir detalles del producto en la respuesta
        representation = super().to_representation(instance)
        representation['producto'] = ProductoSerializer(instance.producto).data
        return representation

class SolicitudCompraSerializer(serializers.ModelSerializer):
    proveedor_id = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all(), source='proveedor', write_only=True)
    proveedor = ProveedorSerializer(read_only=True)
    items = ItemCompraSerializer(many=True, required=False)
    class Meta:
        model = SolicitudCompra
        fields = '__all__'
        
