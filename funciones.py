import json
from datetime import datetime

ARCHIVO = "datos.json"
ARCHIVO_VENTAS = "ventas.json"

# CARGAR DATOS

def cargar_datos():
    """
    Carga los datos desde JSON.
    Si el archivo está vacío, carga cómics base.
    """
    try:
        with open(ARCHIVO, "r") as file:
            comics = json.load(file)

            if not comics:  # Si está vacío
                comics = comics_base()
                guardar_datos(comics)

            return comics

    except FileNotFoundError:
        comics = comics_base()
        guardar_datos(comics)
        return comics
# ======================================================
# COMICS BASE (INICIALES)
# ======================================================
def comics_base():
    """
    Devuelve una lista de cómics iniciales.
    Se usa si el archivo está vacío.
    """
    return [
        {"nombre": "Batman Año Uno", "categoria": "DC", "precio": 15.0, "stock": 5, "fecha": "Inicial"},
        {"nombre": "Spider-Man Blue", "categoria": "Marvel", "precio": 18.0, "stock": 3, "fecha": "Inicial"},
        {"nombre": "Watchmen", "categoria": "DC", "precio": 22.5, "stock": 2, "fecha": "Inicial"},
        {"nombre": "Saga Vol.1", "categoria": "Independiente", "precio": 20.0, "stock": 4, "fecha": "Inicial"},
    ]

# ======================================================
# GUARDAR DATOS
# ======================================================
def guardar_datos(comics):
    """
    Guarda la lista de cómics en el archivo JSON.
    Se usa para mantener persistencia de datos.
    """
    with open(ARCHIVO, "w") as file:
        json.dump(comics, file, indent=4)


# ======================================================
# AGREGAR COMIC
# ======================================================
def agregar_comic(comics):
    """
    Solicita datos al usuario, valida entradas
    y agrega un nuevo cómic al inventario.
    """
    nombre = input("Nombre del cómic: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    categoria = input("Categoría: ").strip()
    if not categoria:
        print("La categoría no puede estar vacía.")
        return

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("⚠ Precio y stock deben ser valores numéricos.")
        return

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    nuevo = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "fecha": fecha
    }

    comics.append(nuevo)
    guardar_datos(comics)

    print("Cómic agregado correctamente.")

# ======================================================
# MOSTRAR COMICS
# ======================================================

def mostrar_comics(comics):
    """
    Muestra todos los cómics registrados
    indicando si están disponibles o agotados.
    """
    if not comics:
        print("No hay cómics registrados.")
        return

    print("\n📚 INVENTARIO DISPONIBLE")

    for i, comic in enumerate(comics, 1):
        estado = "Disponible" if comic["stock"] > 0 else "Agotado"

        print(f"\n{i}. {comic['nombre']}")
        print(f"   Categoría: {comic['categoria']}")
        print(f"   Precio: ${comic['precio']}")
        print(f"   Stock: {comic['stock']}")
        print(f"   Estado: {estado}")

# ======================================================
# REPORTE TOTAL INVENTARIO
# ======================================================
def reporte_total(comics):
    """
    Calcula el valor total del inventario
    multiplicando precio por stock.
    """
    total = sum(c["precio"] * c["stock"] for c in comics)
    print(f"\n Valor total del inventario: ${total}")


# ======================================================
# FILTRAR POR CATEGORIA
# ======================================================
def filtrar_categoria(comics):
    """
    Permite mostrar solo los cómics
    que pertenecen a una categoría específica.
    """
    categoria = input("Ingrese categoría a buscar: ").strip()

    filtrados = [c for c in comics if c["categoria"].lower() == categoria.lower()]

    if not filtrados:
        print("No se encontraron cómics en esa categoría.")
        return

    for comic in filtrados:
        print(f"- {comic['nombre']} (${comic['precio']})")


# ======================================================
# EXPORTAR INVENTARIO A TXT
# ======================================================
def exportar_txt(comics):
    """
    Exporta todo el inventario a un archivo TXT.
    Sirve como respaldo adicional.
    """
    with open("reporte_inventario.txt", "w") as file:
        for comic in comics:
            file.write(f"{comic['nombre']} - {comic['categoria']} - ${comic['precio']} - Stock: {comic['stock']}\n")

    print("Inventario exportado a reporte_inventario.txt")


# # ======================================================
# CARGAR VENTAS
# ======================================================
def cargar_ventas():
    try:
        with open(ARCHIVO_VENTAS, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def guardar_ventas(ventas):
    with open(ARCHIVO_VENTAS, "w") as file:
        json.dump(ventas, file, indent=4)


# ======================================================
# VENDER COMIC
# ======================================================
def vender_comic(comics):
    """
    Permite vender un cómic.
    Reduce el stock y guarda la venta en ventas.json
    """
    mostrar_comics(comics)

    nombre = input("\nIngrese nombre del cómic a vender: ").strip()

    for comic in comics:
        if comic["nombre"].lower() == nombre.lower():

            if comic["stock"] <= 0:
                print("No hay stock disponible.")
                return

            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                print("⚠ Debe ingresar un número.")
                return

            if cantidad > comic["stock"]:
                print("No hay suficiente stock.")
                return

            comic["stock"] -= cantidad
            guardar_datos(comics)

            ventas = cargar_ventas()
            venta = {
                "nombre": comic["nombre"],
                "cantidad": cantidad,
                "total": cantidad * comic["precio"],
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
            }

            ventas.append(venta)
            guardar_ventas(ventas)

            print("Venta realizada con éxito.")
            return

    print("Cómic no encontrado.")


# ======================================================
# BUSCAR COMIC
# ======================================================
def buscar_comic(comics):
    """
    Busca un cómic por nombre.
    """
    nombre = input("Ingrese nombre a buscar: ").strip()

    encontrados = [c for c in comics if nombre.lower() in c["nombre"].lower()]

    if not encontrados:
        print("No se encontraron resultados.")
        return

    for comic in encontrados:
        print(f"{comic['nombre']} - Stock: {comic['stock']}")


# ======================================================
# REPORTE AGOTADOS
# ======================================================
def reporte_agotados(comics):
    """
    Muestra cómics con stock 0.
    """
    agotados = [c for c in comics if c["stock"] == 0]

    if not agotados:
        print("No hay cómics agotados.")
        return

    print("\n CÓMICS AGOTADOS:")
    for comic in agotados:
        print(f"- {comic['nombre']}")
