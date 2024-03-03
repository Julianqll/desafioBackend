from rest_framework import serializers
from .models import Proveedor, Producto, SolicitudCompra, ItemCompra

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ItemCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompra
        fields = '__all__'

class SolicitudCompraSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer()
    items = ItemCompraSerializer(many=True)

    class Meta:
        model = SolicitudCompra
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        solicitud = SolicitudCompra.objects.create(**validated_data)
        for item_data in items_data:
            ItemCompra.objects.create(solicitud=solicitud, **item_data)
        solicitud.calcular_precio_total()
        return solicitud

    def update(self, instance, validated_data):
        instance.proveedor = validated_data.get('proveedor', instance.proveedor)
        instance.aprobada = validated_data.get('aprobada', instance.aprobada)
        
        items_data = validated_data.get('items')
        if items_data:
            instance.items.all().delete()
            for item_data in items_data:
                ItemCompra.objects.create(solicitud=instance, **item_data)
            instance.calcular_precio_total()

        instance.save()
        return instance
