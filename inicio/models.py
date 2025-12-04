from django.db import models

from django.utils import timezone

class Departamento(models.Model):

    # Crear atributo id auto incrementable
    id = models.AutoField(primary_key=True)

    # Crear atributo nombre (texto)
    nombre = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):

    # Crear atributo id auto incrementable
    id = models.AutoField(primary_key=True)

    # Crear atributo nombre (texto)
    nombre = models.CharField(max_length=100, default="")

    # Crear atributo dirección (texto)
    direccion = models.CharField(max_length=100, default="")

    rfc = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    # Crear atributo id auto incrementable
    id = models.AutoField(primary_key=True)

    # Crear atributo nombre (texto)
    nombre = models.CharField(max_length=100, default="")

    # Campo que asocia el producto con su proveedor
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    # Campo que asocia el producto con su departamento (belleza, higiene, perfumeria, etc)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    # Campo que muestra la imagen del producto
    # Se recomienda que sea una URL para mayor facilidad y no depender de almacenamiento interno
    imagen = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.nombre




# class Inventario(models.Model):
#     # Crear atributo id auto incrementable
#     id = models.AutoField(primary_key=True)

#     # Campo que asocia el producto con su inventario
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
#     # Campo que indica el stock disponible de cada producto
#     stock = models.PositiveIntegerField(default=0)


class HistorialInventario(models.Model):
    # Crear atributo id auto incrementable
    id = models.AutoField(primary_key=True)

    # Campo que asocia el producto con su historial
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    # Campo que indica el stock disponible de cada producto
    # stock_previo = models.PositiveIntegerField(default=0) (pienso si es necesario)

    # Campo que indica el stock disponible de cada producto
    stock = models.PositiveIntegerField(default=0)

    # Campo que indica en qué fecha se actualizo el inventario
    # Permite conocer el historial de cada producto
    fecha = models.DateTimeField(default=timezone.now)

class Precio(models.Model):
    # Crear atributo id auto incrementable
    id = models.AutoField(primary_key=True)

    # Campo que asocia el producto con su precio
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='precio')

    # Campo que indica el precio 
    # Desde aquí debería obtenerse el precio del producto para que siempre esté actualizado
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    # Campo que indica si es promoción
    es_promocion = models.BooleanField(default=False)

    # Campo que indica el motivo de la promoción (navidad, halloween, etc)
    motivo = models.CharField(max_length=100, default="")

#CADA QUE SE HAGA UN CAMBIO EN ESTE ARCHIVO HAY QUE EJECUTAR LOS SIGUIENTES COMANDOS
#python manage.py makemigrations
#python manage.py migrate
    






    

