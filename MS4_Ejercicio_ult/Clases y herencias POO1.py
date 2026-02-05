#Plataforma de gestions de usuarios Brandon Chilaquies Corp.
class User: #Clase base

    def __init__(self, nombre, cargo, email):
        self._nombre = nombre      # Atributo protegido
        self._email = email
        self._cargo = cargo

    def mostrar_info(self): #Método que será redefinido por las clases hijas.
        return f"Usuario: {self._nombre} | cargo: {self._cargo} | Email: {self._email}"


class UserAdmin(User):  #Clase hija usuario administrador.
    def mostrar_info(self):#Redefinición del método
        return f"Usuario: {self._nombre} | cargo: {self._cargo} | Email: {self._email}"


class UserClient(User): #Clase hija que representa usuario cliente.
    

    def mostrar_info(self): #Redefinición del método (polimorfismo).
        return f"Usuario: {self._nombre} | cargo: {self._cargo} | Email: {self._email}"

# Prueba del sistema
usuario1 = UserAdmin("Brandon","CEO de Chilaquiles Corp.", "Brandonadmin@chilaquilescorp.com")
usuario2 = UserClient("Megano","Desarrollador(frontdesk) ","menganito@chilaquilescorp.com")

print(usuario1.mostrar_info())
print(usuario2.mostrar_info())


#Principio de POO en cada clase
"""
Las clases UserAdmin y UserClient heredan de la clase Usuario, reutilizando sus atributos y estructura.
Se aplica el polimorfismo al redefinir el método mostrar_info, lo que permite comportamientos distintos dependiendo del tipo de usuario.

"""

#UML simple
"""
┌───────────────────────────┐
│         Usuario           │
├───────────────────────────┤
│ - _nombre : str           │
│ - _cargo  : str           │
│ - _email  : str           │
├───────────────────────────┤
│ + mostrar_info() : str    │
└─────────────▲─────────────┘
              │
      ┌───────┴────────┐
      │                │
┌───────────────┐  ┌────────────────┐
│ UsuarioAdmin  │  │ UsuarioCliente │
├───────────────┤  ├────────────────┤
│               │  │                │
├───────────────┤  ├────────────────┤
│ + mostrar_info│  │ + mostrar_info │
│   () : str    │  │   () : str     │
└───────────────┘  └────────────────┘

"""