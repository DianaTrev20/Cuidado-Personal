from django.db import models
from django.core.validators import MinValueValidator 

# --- MODELO 1: PROVEEDOR ---
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    contacto_nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# --- MODELO 2: CATEGORIA ---
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

# --- MODELO 3: PRODUCTO ---
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    
    # SEGURIDAD EN LA BD: INTEGRIDAD DE DATOS
    # MinValueValidator(0) asegura que el stock nunca sea negativo
    stock_actual = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)] 
    )
    
    stock_minimo = models.IntegerField(
        default=10, 
        validators=[MinValueValidator(0)]
    )
    
    # El precio debe ser al menos 0.01 (no puede ser 0 ni negativo)
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} ({self.stock_actual} en stock)"