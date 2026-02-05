import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget
)

class VentanaJugador(QWidget): #herencia
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion Gamer")
        self.setGeometry(200, 200, 400, 350)

        self.layout = QVBoxLayout() #Layout principal

        #widgets
        self.label_nombre = QLabel("Nombre del Jugador: ")
        self.input_nombre = QLineEdit()

        self.label_juego = QLabel("Videojuego favorito: ")
        self.input_juego = QLineEdit()

        self.boton_agregar = QPushButton("Registrar jugador")
        self.lista_jugador = QListWidget()  # CORREGIDO

        #agregar los widgets al layout
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)
        self.layout.addWidget(self.label_juego)
        self.layout.addWidget(self.input_juego)
        self.layout.addWidget(self.boton_agregar)
        self.layout.addWidget(self.lista_jugador)

        self.setLayout(self.layout)

        #señal y slot
        self.boton_agregar.clicked.connect(self.agregar_jugador)

    # CORREGIDO: ahora sí está dentro de la clase
    def agregar_jugador(self):
        nombre = self.input_nombre.text()
        juego = self.input_juego.text()

        if nombre and juego:
            self.lista_jugador.addItem(f"{nombre} - {juego}")
            self.input_nombre.clear()
            self.input_juego.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaJugador()
    ventana.show()
    sys.exit(app.exec_())



"""
En esta parte hice una aplicación de escritorio usando PyQt5 pero enfocada en usuarios gamers. La idea es que se puedan registrar jugadores con su nombre y su videojuego favorito, y que esos datos se muestren en una lista dentro de la misma ventana.

La clase principal se llama VentanaJugador y hereda de QWidget. Eso significa que estamos usando herencia, porque la clase toma todas las características básicas de una ventana que ya trae PyQt. Gracias a eso puedo usar métodos como setWindowTitle(), setGeometry() y show() sin tener que crear todo desde cero.

Dentro de la clase agregué varios widgets: QLabel para los textos, QLineEdit para que el usuario escriba el nombre y el juego, QPushButton para registrar al gamer y QListWidget para mostrar la lista de jugadores registrados. También usé un QVBoxLayout para organizar todo verticalmente.

Para manejar los eventos utilicé el sistema de señales y slots. Por ejemplo, cuando el botón se presiona, se activa la señal clicked, y con connect() la enlazo al método registrar_gamer. Entonces cuando el usuario hace clic, automáticamente se ejecuta esa función y se agrega el gamer a la lista.

PyQt es orientado a objetos porque todo funciona con clases y objetos. Cada widget es una clase, y cuando lo usamos estamos creando instancias. También aplicamos herencia al extender QWidget. Básicamente todo el framework está construido bajo los principios de la programación orientada a objetos.


"""