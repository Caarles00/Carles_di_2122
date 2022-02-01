import sys
import os

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QDialog,
    QDialogButtonBox
)

ruta_base = os.path.dirname(__file__)

# Dialeg per a exir
class DialogExit(QDialog):
    # Indiquem que no te pare per a que aparegua damunt de la finstra
    def __init__(self, parent=None):
        super().__init__(parent)

        # Dialegs
        self.setWindowTitle("Dialeg eixir")

        self.buttons_dialog = QDialogButtonBox.Yes | QDialogButtonBox.No
        
        self.buttons_dialog = QDialogButtonBox(self.buttons_dialog)
        self.buttons_dialog.accepted.connect(self.accept)
        self.buttons_dialog.rejected.connect(self.reject)

        self.layout_dialeg = QVBoxLayout()
        mensatgeEixir = QLabel("Estas segur de que vols eixir?")
        self.layout_dialeg.addWidget(mensatgeEixir)
        self.layout_dialeg.addWidget(self.buttons_dialog)
        self.setLayout(self.layout_dialeg)

# Pantalla Admin
class Admin(QMainWindow):
    def __init__(self):
        super().__init__()

        admin = QVBoxLayout()
        self.setWindowTitle("ADMIN")
        self.label = QLabel("Has entrat com a administrador")
        self.setCentralWidget(self.label)

        icon_path = os.path.join(ruta_base, "PNGs/door-open-out.png")
        LogOut = QAction(QIcon(icon_path), "&Log out", self)
        LogOut.setStatusTip("Log out")
        LogOut.triggered.connect(self.tornarLogin)

        icon_path = os.path.join(ruta_base, "PNGs/cross-button.png")
        salir = QAction(QIcon(icon_path), "&Salir", self)
        salir.setStatusTip("Salir")
        salir.triggered.connect(self.exit)

        menu = self.menuBar()

        menu_action = menu.addMenu("&Options")
        menu_action.addAction(LogOut)
        menu_action.addAction(salir)


    # Tornar a la pantalla de login
    def tornarLogin(self):
        self.hide()
        if (__name__ == '__main__'):
            self = MainWindow()
            if (__name__ == '__main__'):
                w.show()

    # Eixir
    def exit(self):
        dlg = DialogExit()
        if dlg.exec_():
            app.closeAllWindows()
        else:
            pass

# Pantalla User
class User(QMainWindow):
    def __init__(self):
        super().__init__()

        user = QVBoxLayout()
        self.setWindowTitle("USER")
        self.label = QLabel("Has entrat com a usuari", self)
        self.setCentralWidget(self.label)

        icon_path = os.path.join(ruta_base, "PNGs/door-open-out.png")
        LogOut = QAction(QIcon(icon_path), "&Log out", self)
        LogOut.setStatusTip("Log out")
        LogOut.triggered.connect(self.tornarLogin)

        icon_path = os.path.join(ruta_base, "PNGs/cross-button.png")
        salir = QAction(QIcon(icon_path), "&Salir", self)
        salir.setStatusTip("Salir")
        salir.triggered.connect(self.exit)

        menu = self.menuBar()

        menu_action = menu.addMenu("&Options")
        menu_action.addAction(LogOut)
        menu_action.addAction(salir)


    # Tornar a la pantalla de Login
    def tornarLogin(self):
        self.hide()
        if (__name__ == '__main__'):
            self = MainWindow()
            if (__name__ == '__main__'):
                w.show()

    #  Eixir
    def exit(self):
        dlg = DialogExit()
        if dlg.exec_():
            app.closeAllWindows()
        else:
            pass


# Pantalla Login
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        self.user = User()
        self.admin = Admin()

        layout = QVBoxLayout()

        self.label = QLabel("", self)

        # Creem el LineEdit per a l'usuari
        self.usuari = QLineEdit()
        self.usuari.setPlaceholderText("Usuario")
        layout.addWidget(self.usuari)

        # Creem el LineEdit per a la contrasenya
        self.passwd = QLineEdit()
        self.passwd.setPlaceholderText("Contraseña")
        layout.addWidget(self.passwd)

        # Creem el botó
        button = QPushButton("Login")
        button.clicked.connect(self.checkIn)
        layout.addWidget(button)

        icon_path = os.path.join(ruta_base, "PNGs/cross-button.png")
        salir = QAction(QIcon(icon_path), "&Salir", self)
        salir.setStatusTip("Salir")
        salir.triggered.connect(self.exit)

        menu = self.menuBar()

        menu_principal = menu.addMenu("&Options")
        menu_principal.addAction(salir)

        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Funcio per a entrar en la pantalla indicada
    def checkIn(self):
        if self.usuari.text() == "admin" and self.passwd.text() == "1234":
            self.admin.show()
        elif self.usuari.text() == "user" and self.passwd.text() == "1234":
            self.user.show()
        else:
            self.label.setText("Nom d'usuari o contrasenya incorrectes")
    
    #  Eixir
    def exit(self):
        dlg = DialogExit()
        if dlg.exec_():
            app.closeAllWindows()
        else:
            pass



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()