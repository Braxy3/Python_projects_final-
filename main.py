from funciones import *


def login():
    """
    Verifica usuario y contraseña.
    Permite acceso solo si las credenciales coinciden.
    """
    usuario_correcto = "braxy"
    contraseña_correcta = "1234"

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        return True
    else:
        print("Credenciales incorrectas")
        return False


def menu():
    comics = cargar_datos()

    while True:
        print("\n=== TIENDA DE COMICS ===")
        print("1. Agregar cómic")
        print("2. Mostrar cómics")
        print("3. Vender cómic")
        print("4. Buscar cómic")
        print("5. Reporte total inventario")
        print("6. Reporte agotados")
        print("7. Filtrar por categoría")
        print("8. Exportar inventario")
        print("9. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            agregar_comic(comics)
        elif opcion == "2":
            mostrar_comics(comics)
        elif opcion == "3":
            vender_comic(comics)
        elif opcion == "4":
            buscar_comic(comics)
        elif opcion == "5":
            reporte_total(comics)
        elif opcion == "6":
            reporte_agotados(comics)
        elif opcion == "7":
            filtrar_categoria(comics)
        elif opcion == "8":
            exportar_txt(comics)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("⚠ Opción inválida")


if __name__ == "__main__":
    if login():
        menu()
