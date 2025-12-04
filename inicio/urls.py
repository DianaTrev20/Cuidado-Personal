from django.urls import path
from . import views

# Urls válidas para el módulo escuela
urlpatterns = [

    # http://localhost:8000/productos  --> obtenerproductos
    path('productos', views.obtenerproductos, name="obtener_productos"),

    # http://localhost:8000/producto/1  --> detallesproducto
    path('producto/<int:id>', views.detallesproducto, name="detallesproducto"),

    # http://localhost:8000/historialinventario/producto/1  --> detallesproducto
    path('historialinventario/producto/<int:id>', views.historialinventario, name="historialinventario"),


    # http://localhost:8000/crear_producto_form -> crear_producto_form
    path('crear_producto_form', views.crear_producto_form),


    # http://localhost:8000/crear_producto -> crear_producto
    path('crear_producto', views.crear_producto, name="crear_producto"),

    
    # http://localhost:8000/historial_inventario_form -> historial_inventario_form
    path('historial_inventario_form', views.historial_inventario_form),


    # http://localhost:8000/registrar_inventario -> registrar_inventario
    path('registrar_inventario', views.registrar_inventario, name="registrar_inventario"),


    

]