# productos/urls.py
from django.urls import path
from .views import (
    # Vistas de Productos
    ProductoListView, 
    ProductoCreateView, 
    ProductoDetailView, 
    ProductoUpdateView, 
    ProductoDeleteView,
    comprar_producto, # Función de compra

    # Vistas de Proveedores
    ProveedorListView, 
    ProveedorCreateView, 
    ProveedorDetailView, 
    ProveedorUpdateView, 
    ProveedorDeleteView,

    reporte_exportar
)

urlpatterns = [
    # --- RUTAS DE PRODUCTO ---
    path('', ProductoListView.as_view(), name='producto_list'), 
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'), 
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'), 
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'), 
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'), 
    path('<int:pk>/comprar/', comprar_producto, name='producto_comprar'),

    # NUEVA RUTA PARA EL REPORTE
    path('reporte/', reporte_exportar, name='reporte_stock'),

    # --- RUTAS DE PROVEEDOR ---
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'), 
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor_create'), 
    path('proveedores/<int:pk>/', ProveedorDetailView.as_view(), name='proveedor_detail'), 
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_update'), 
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_delete'), 
]