from django.db import models

class Categoria(models.Model):
    """
    Representa una categoría de productos.
    Una categoría puede tener muchos productos.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """
    Representa un producto dentro del sistema.
    Cada producto pertenece a una categoría.
    """
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre
