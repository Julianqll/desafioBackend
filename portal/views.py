from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from portal.models import ItemCompra, Producto, Proveedor, SolicitudCompra
from portal.serializer import ItemCompraSerializer, ProductoSerializer, ProveedorSerializer, SolicitudCompraSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class LoginViewSet(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = get_object_or_404(User, username=username)

        if not user.check_password(password):
            return Response({"details": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)

        return Response({"token": token.key, "user": serializer.data})

class ProveedorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

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