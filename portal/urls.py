from django.urls import path, include
from rest_framework import routers

from portal import views

router = routers.DefaultRouter()
router.register(r'proveedores', views.ProveedorViewSet, 'proveedores')
router.register(r'productos', views.ProductoViewSet, 'productos')
router.register(r'solicitudescompra', views.SolicitudCompraViewSet, 'solicitudescompra')

urlpatterns =[
    path("api/v1/", include(router.urls))
]