"""
PROYECTO: Minimarket con Django

Este proyecto es una aplicación web hecha con Django para administrar
productos y categorías de un minimarket.

Modelos:
- Categoria: guarda el nombre y descripción de cada categoría.
- Producto: guarda nombre, precio, stock y pertenece a una categoría.

Relación:
Una categoría puede tener muchos productos.
Cada producto pertenece a una sola categoría.

Cómo funciona el flujo del sistema:

1. El usuario entra al navegador (http://127.0.0.1:8000/productos/).
2. Django recibe la petición.
3. La URL llama a una vista (ListView).
4. La vista consulta los productos en la base de datos usando el modelo.
5. Django envía los datos al template (archivo HTML).
6. El template muestra la información en pantalla.

El proyecto usa Programación Orientada a Objetos porque:
- Los modelos son clases.
- Las vistas basadas en clases usan herencia.
- Cada clase organiza su propia información.

Django usa un ORM que convierte automáticamente las clases en tablas
de la base de datos sin necesidad de escribir SQL.
"""

