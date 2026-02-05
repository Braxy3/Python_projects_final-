from django.urls import path
from .views import (
    ListaProductosView,
    CrearProductoView,
    CrearCategoriaView,
)

urlpatterns = [
    path("", ListaProductosView.as_view(), name="lista_productos"),
    path("crear/", CrearProductoView.as_view(), name="crear_producto"),
    path("categoria/crear/", CrearCategoriaView.as_view(), name="crear_categoria"),
]
