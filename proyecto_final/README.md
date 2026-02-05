# Sistema de Gestión – Tienda de Cómics

## Descripción

Este proyecto es un sistema de gestión en consola desarrollado en Python para administrar el inventario de una tienda de cómics.

El sistema permite registrar, consultar, vender y analizar productos, manteniendo la información almacenada de manera persistente mediante archivos JSON.

El programa está estructurado en módulos separados para mejorar la organización y comprensión del código.

---

## Objetivos del sistema

- Gestionar inventario de cómics
- Registrar ventas
- Generar reportes
- Mantener persistencia de datos
- Validar entradas del usuario
- Simular un sistema real de negocio en consola

---

## Estructura del Proyecto

proyecto_final/
│
├── main.py
├── funciones.py
├── datos.json
├── ventas.json
└── README.md

---

## Cómo ejecutar el programa

1. Abrir la terminal dentro de la carpeta proyecto_final
2. Ejecutar:

python main.py

3. Ingresar credenciales:

Usuario: admin  
Contraseña: 1234

---

## Funcionalidades del Sistema

Login  
Sistema básico de autenticación con usuario y contraseña.

Inventario Base  
El sistema carga automáticamente cómics iniciales si el archivo está vacío.

Agregar Cómics  
Permite registrar nuevos productos con:
- Nombre
- Categoría
- Precio
- Stock
- Fecha automática

Mostrar Inventario  
Lista todos los cómics indicando:
- Precio
- Stock disponible
- Estado (Disponible / Agotado)

Vender Cómics  
- Reduce el stock
- Registra la venta en ventas.json
- Guarda fecha y total de la venta

Buscar por Nombre  
Permite encontrar cómics por coincidencia parcial.

Reporte Total  
Calcula el valor total del inventario (precio × stock).

Reporte de Agotados  
Muestra cómics con stock igual a 0.

Filtro por Categoría  
Permite visualizar cómics de una categoría específica.

Exportar Inventario  
Genera un archivo reporte_inventario.txt con todos los productos.

---

## Persistencia de Datos

El sistema utiliza:

- datos.json → almacena inventario
- ventas.json → almacena historial de ventas

Los datos:
- Se cargan al iniciar el programa
- Se guardan automáticamente al modificar información
- No se pierden al cerrar el sistema

---

## Validaciones Implementadas

- Evita entradas vacías
- Evita letras donde deben ir números
- Maneja errores con try / except
- Valida existencia de stock antes de vender
- Controla opciones inválidas del menú

---

## Estructuras de Datos Utilizadas

- Listas
- Diccionarios
- Diccionarios dentro de listas (estructura principal)
- Archivos JSON para almacenamiento persistente

---

## Ejemplo de Uso

1. Agregar cómic  
Nombre: One Piece Vol.1  
Categoría: Manga  
Precio: 12  
Stock: 10  

2. Vender cómic  
Nombre: One Piece Vol.1  
Cantidad: 2  

Stock actualizado correctamente.

---

## Conceptos Aplicados

- Programación modular
- Manejo de archivos
- Validación de datos
- Persistencia con JSON
- Control de flujo con menús interactivos
- Simulación de sistema real de gestión

---

## Autor

Proyecto desarrollado como sistema de gestión académico en Python.
