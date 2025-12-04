from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

# Importar los modelos
from .models import *

# Importar las clases que generan los formularios para insertar datos en los modelos
from .forms import *

# Crear la función obteneralumnos
def obtenerproductos(peticion):

    # Obtener datos de la BD
    # Del modelo Producto
    productos = list(Producto.objects.all().select_related('precio'))

    # Crear un objeto json con los datos que se muestran
    # al usuario
    datos = {
        'mensaje': 'Datos obtenidos exitosamente',
        'productos': productos
    }

    # Regresar al usuario una página html
    return render(peticion, 'productos.html', datos)


# Crear la función obteneralumnos
def detallesproducto(peticion, id):

    # Obtener datos de la BD
    # Del modelo Producto por el id del producto
    producto = get_object_or_404(Producto.objects.select_related('precio'), id=id)

    # Crear un objeto json con los datos que se muestran
    # al usuario
    datos = {
        'mensaje': 'Datos obtenidos exitosamente',
        'producto': producto
    }

    # Regresar al usuario una página html
    return render(peticion, 'detallesproducto.html', datos)

# Crear la función historialinventario
def historialinventario(peticion, id):

    # Obtener datos de la BD
    # Del modelo HistorialInventario por el id del producto
    historial = get_list_or_404(HistorialInventario.objects, producto=id)

    # Crear un objeto json con los datos que se muestran
    # al usuario
    datos = {
        'mensaje': 'Datos obtenidos exitosamente',
        'historial': historial
    }

    # Regresar al usuario una página html
    return render(peticion, 'historialinventario.html', datos)


def crear_producto_form(peticion):

    # Crear un nuevo formulario con el modelo de formulario que creamos previamente
    form = ProductoForm()
    
    # Regresar al usuario una página html
    return render(peticion, 'crear_producto.html', {'form': form})


# Crear la función que RECIBE los datos del formulario de crear alumno
def crear_producto(request):

    # Recibimos los datos
    datos = ProductoForm(request.POST)

    # Validad que sean datos correctos
    if datos.is_valid():
        # Guardar los datos del nuevo alumno
        datos.save()

        # Mandar al usuario a otra ruta
        return redirect('obtener_productos') 
    

def historial_inventario_form(peticion):

    # Crear un nuevo formulario con el modelo de formulario que creamos previamente
    form = HistorialInventarioForm
    
    # Regresar al usuario una página html
    return render(peticion, 'inventario_form.html', {'form': form})


# Crear la función que RECIBE los datos del formulario de crear alumno
def registrar_inventario(request):

    # Recibimos los datos
    datos = HistorialInventarioForm(request.POST)

    # Validad que sean datos correctos
    if datos.is_valid():
        # Guardar los datos del nuevo alumno
        datos.save()

        # Mandar al usuario a otra ruta
        return redirect('obtener_productos') 
    

