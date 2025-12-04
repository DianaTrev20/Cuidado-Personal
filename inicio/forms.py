# Importar la libreria de django para crear formularios
from django import forms
# Importar todos los modelos
from .models import *

# Crear un modelo de formulario para el Historial del Inventario
class HistorialInventarioForm(forms.ModelForm):
    class Meta:

        model = HistorialInventario

        # Campos que tendrá el formulario
        fields = ["producto", "stock", "fecha"]

# Crear un modelo de formulario para Producto
class ProductoForm(forms.ModelForm):
    class Meta:

        model = Producto

        # Campos que tendrá el formulario
        fields = ["nombre", "proveedor", "departamento", "imagen"]

