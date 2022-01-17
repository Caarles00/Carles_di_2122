import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                               QGridLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QStackedLayout, QStatusBar,
                               QVBoxLayout, QWidget)

ruta_base = os.path.dirname(__file__)

'''
-----------------------------------------------------------------------
No trobe el error que tinc, no m'apareixen els QLineEdits ni el botó.
La meua intenció es fer un QStackedLayout de la finestra del login, i 
despres de quan entres com a admin o com a user
----------------------------------------------------------------------- 
'''

# Dialeg per a el log out
class DialogLogOut(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Dialegs
        self.setWindowTitle("Dialeg log out")

        self.buttons_dialog = QDialogButtonBox.Yes | QDialogButtonBox.No
        
        self.buttons_dialog = QDialogButtonBox(self.buttons_dialog)
        self.buttons_dialog.accepted.connect(self.accept)
        self.buttons_dialog.rejected.connect(self.reject)

        self.layout_dialeg = QVBoxLayout()
        mensatgeLogOut = QLabel("Estas segur de que vols fer el log out?")
        self.layout_dialeg.addWidget(mensatgeLogOut)
        self.layout_dialeg.addWidget(self.buttons_dialog)
        self.setLayout(self.layout_dialeg)

# Dialeg per a exir
class DialogExit(QDialog):
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.user = "user"
        self.admin = "admin"
        self.passwd = 1234

        self.setWindowTitle("Finestra Login")

        self.widget = QWidget()
        

        # Creem el stacked layout
        self.stackedLayout = QStackedLayout(self.widget)

        # Creem widget i layout per a la pantalla del user: admin
        self.pantallaAdmin = QWidget()
        self.layoutAdmin = QVBoxLayout(self.pantallaAdmin)
        self.pantallaAdmin.setLayout(self.layoutAdmin)

        # Creem widget i layout per a la pantalla del user: user
        self.pantallaUser = QWidget()
        self.layoutUser = QVBoxLayout(self.pantallaUser)
        self.pantallaUser.setLayout(self.layoutUser)

        # Creem widget i layout per a la pantalla del login
        self.pantallaLogin = QWidget()
        self.layoutLogin = QVBoxLayout(self.pantallaLogin)
        self.pantallaLogin.setLayout(self.layoutLogin)

        # PANTALLA DEL LOGIN
        layout = QVBoxLayout()

        # Nom de l'usuari
        self.lineUser = QLineEdit()
        self.lineUser.setMaxLength(15)
        self.lineUser.setPlaceholderText("User name")
        layout.addWidget(self.lineUser)

        # Contrasenya
        self.linePasswd = QLineEdit()
        self.linePasswd.setMaxLength(15)
        self.linePasswd.setPlaceholderText("Password")
        layout.addWidget(self.linePasswd)

        # Botó de login
        self.loginButton = QPushButton("Login")
        layout.addWidget(self.loginButton)
        self.loginButton.clicked.connect(self.checkIn)

        # Afegim el layout del login a la pantalla corresponent
        self.layoutLogin.addLayout(layout)


        # PANTALLA DEL USER: ADMIN
        self.labelAdmin = QLabel("Pantalla del usuari admin")
        self.layoutAdmin2 = QVBoxLayout()
        # Afegim el layout del login a la pantalla corresponent
        self.layoutAdmin2.addWidget(self.labelAdmin)


        # PANTALLA DEL USER: USER
        self.labelUser = QLabel("Pantalla dle usuari user")
        self.layoutUser2 = QVBoxLayout()
        # Afegim el layout del login a la pantalla corresponent
        self.layoutUser2.addWidget(self.labelUser)


        # Afegim els widgets al stacked layout
        self.stackedLayout.addWidget(self.pantallaUser)
        self.stackedLayout.addWidget(self.pantallaAdmin)
        self.stackedLayout.addWidget(self.pantallaLogin)

        # Button action del Log out
        icon_path = os.path.join(ruta_base, "PNGs/door-open-out.png")
        self.buttonLogOut = QAction(QIcon(icon_path), "Log out", self)
        self.buttonLogOut.setStatusTip("Log out")
        self.buttonLogOut.triggered.connect(self.checkIn)

        # Button action de eixir
        icon_path = os.path.join(ruta_base, "PNGs/cross-button.png")
        self.buttonExit = QAction(QIcon(icon_path), "Exit", self)
        self.buttonExit.setStatusTip("exit")
        self.buttonLogOut.triggered.connect(self.checkIn)

        # Creem el menu
        menu = self.menuBar()

        # Afegim els submenus
        file_menu = menu.addMenu("&Options")
        file_menu.addAction(self.buttonLogOut)
        file_menu.addAction(self.buttonExit)

        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    # Funcio per a entrar en la pantalla indicada
    def checkIn(self):
        if (self.lineUser.text == self.user) and (self.linePasswd == 1234):
            self.stackedLayout.setCurrentWidget(self.pantallaUser)
        elif (self.lineUser.text == self.admin) and (self.linePasswd == 1234):
            self.stackedLayout.setCurrentWidget(self.pantallaAdmin)
        else:
            print("Nom d'usuari o contrasenya incorrectes")
            exit()

    # Eixir
    def eixir(self):
        dlg = DialogExit()
        if dlg.exec_():
            exit()
        else:
            pass
    
    # Log out
    def LogOut(self):
        dlg = DialogLogOut()
        if dlg.exec_():
            self.stackedLayout.setCurrentWidget(self.pantallaLogin)
        else:
            pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()