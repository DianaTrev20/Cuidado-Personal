from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q 

import random
from datetime import timedelta
from decimal import Decimal 

from .models import Producto, Proveedor

# --- FUNCIÓN DE COMPRA RÁPIDA ---
@login_required
def comprar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if producto.stock_actual > 0:
        producto.stock_actual -= 1
        producto.save()
        messages.success(request, f'¡Compra exitosa! Has comprado: {producto.nombre}')
    else:
        messages.error(request, '¡Lo sentimos! Este producto está agotado.')
        
    return redirect('producto_list')

# --- FUNCIÓN DE REPORTE CON IA DOBLE (STOCK + PRECIOS) ---
@login_required
def reporte_exportar(request):
    productos = Producto.objects.all().order_by('categoria', 'nombre')
    
    # Cálculos Generales
    total_productos = productos.count()
    valor_total_inventario = sum(producto.precio * producto.stock_actual for producto in productos)
    productos_bajos = [p for p in productos if p.stock_actual <= p.stock_minimo]
    cantidad_bajos = len(productos_bajos)

    # CEREBRO DE LA IA
    for p in productos:
        if p.stock_actual > 0:
            # 1. IA PREDICCIÓN DE STOCK
            velocidad_venta_diaria = random.randint(1, 3) 
            dias_restantes = p.stock_actual / velocidad_venta_diaria
            fecha_agotamiento = timezone.now() + timedelta(days=dias_restantes)
            
            p.ia_fecha_agotamiento = fecha_agotamiento
            p.ia_velocidad = velocidad_venta_diaria

            # 2. IA PRECIOS DINÁMICOS
            # Regla 1: Escasez -> SUBIR precio
            if p.stock_actual <= p.stock_minimo:
                p.ia_sugerencia = "SUBIR"
                # CORRECCIÓN AQUÍ: Usamos Decimal('1.15')
                p.ia_precio_sugerido = p.precio * Decimal('1.15') 
                p.ia_motivo = "Alta demanda / Escasez"
                p.ia_color = "success"

            # Regla 2: Sobrestock -> OFERTA
            elif p.stock_actual > 50: 
                p.ia_sugerencia = "OFERTA"
                # CORRECCIÓN AQUÍ: Usamos Decimal('0.90')
                p.ia_precio_sugerido = p.precio * Decimal('0.90')
                p.ia_motivo = "Liberar espacio"
                p.ia_color = "warning"

            # Regla 3: Normal -> MANTENER
            else:
                p.ia_sugerencia = "MANTENER"
                p.ia_precio_sugerido = p.precio
                p.ia_motivo = "Equilibrio ideal"
                p.ia_color = "secondary"

        else:
            p.ia_fecha_agotamiento = None
            p.ia_sugerencia = "REABASTECER"
            p.ia_color = "danger"

    context = {
        'productos': productos,
        'fecha_hoy': timezone.now(),
        'total_productos': total_productos,
        'valor_total_inventario': valor_total_inventario,
        'cantidad_bajos': cantidad_bajos,
    }
    return render(request, 'productos/reporte_stock.html', context)

# --- VISTAS CRUD ---

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q') 
        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(categoria__nombre__icontains=query))
        return queryset

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ['categoria', 'proveedor', 'imagen', 'nombre', 'descripcion', 'stock_actual', 'stock_minimo', 'precio']
    success_url = reverse_lazy('producto_list')

class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ['categoria', 'proveedor', 'imagen', 'nombre', 'descripcion', 'stock_actual', 'stock_minimo', 'precio']
    def get_success_url(self):
        return reverse_lazy('producto_detail', kwargs={'pk': self.object.pk})

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedores/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'proveedores/proveedor_form.html'
    fields = ['nombre', 'contacto_nombre', 'telefono', 'email', 'direccion'] 
    success_url = reverse_lazy('proveedor_list')

class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor
    template_name = 'proveedores/proveedor_detail.html'
    context_object_name = 'proveedor'

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = 'proveedores/proveedor_form.html'
    fields = ['nombre', 'contacto_nombre', 'telefono', 'email', 'direccion']
    def get_success_url(self):
        return reverse_lazy('proveedor_detail', kwargs={'pk': self.object.pk})

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')