from django.urls import path, include, re_path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from portal import views

router = routers.DefaultRouter()
router.register(r'proveedores', views.ProveedorViewSet, 'proveedores')
router.register(r'productos', views.ProductoViewSet, 'productos')
router.register(r'solicitudescompra', views.SolicitudCompraViewSet, 'solicitudescompra')
router.register(r'itemcompras', views.ItemCompraViewSet, 'itemcompras')

urlpatterns =[
    path("api/v1/", include(router.urls)),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name = "schema")),

]