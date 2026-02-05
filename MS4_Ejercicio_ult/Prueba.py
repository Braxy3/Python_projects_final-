import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget
)

class VentanaGamers(QWidget):  # Herencia
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Gamers 🎮")
        self.setGeometry(200, 200, 400, 350)

        # Layout principal
        self.layout = QVBoxLayout()

        # Widgets
        self.label_nombre = QLabel("Nombre del Gamer:")
        self.input_nombre = QLineEdit()

        self.label_juego = QLabel("Videojuego Favorito:")
        self.input_juego = QLineEdit()

        self.boton_agregar = QPushButton("Registrar Gamer")
        self.lista_gamers = QListWidget()

        # Agregar widgets al layout
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)
        self.layout.addWidget(self.label_juego)
        self.layout.addWidget(self.input_juego)
        self.layout.addWidget(self.boton_agregar)
        self.layout.addWidget(self.lista_gamers)

        self.setLayout(self.layout)

        # Señal y Slot
        self.boton_agregar.clicked.connect(self.registrar_gamer)

    def registrar_gamer(self):
        nombre = self.input_nombre.text()
        juego = self.input_juego.text()

        if nombre and juego:
            self.lista_gamers.addItem(f"{nombre} - 🎮 {juego}")
            self.input_nombre.clear()
            self.input_juego.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaGamers()
    ventana.show()
    sys.exit(app.exec_())
