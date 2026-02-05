from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Producto, Categoria


class ListaProductosView(ListView):
    """
    Muestra la lista de todos los productos.
    """
    model = Producto
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"


class CrearProductoView(CreateView):
    """
    Permite crear un nuevo producto.
    """
    model = Producto
    fields = ["nombre", "precio", "stock", "categoria"]
    template_name = "productos/crear_producto.html"
    success_url = reverse_lazy("lista_productos")


class CrearCategoriaView(CreateView):
    """
    Permite crear una nueva categoría.
    """
    model = Categoria
    fields = ["nombre", "descripcion"]
    template_name = "productos/crear_categoria.html"
    success_url = reverse_lazy("lista_productos")
