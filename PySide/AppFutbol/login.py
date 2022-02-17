from ossaudiodev import SOUND_MIXER_TREBLE
import sys
import os
from time import sleep


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
    QDialogButtonBox,
    QComboBox,
    QHBoxLayout,
    QSpinBox
)

ruta_base = os.path.dirname(__file__)

# Connexió al la base de dades
# class ConnexioBD():
#     def __init__(self):
#         super().__init__()

#         def create_table(con):
#             cursor = con.cursor()
#             try:
#                 cursor.execute("CREATE TABLE IF NOT EXISTS Entrenadors(nom CHAR, passwd CHAR)")
#                 print("Taula creada")
#             except sqlite3.OperationalError:
#                 print("La taula de Entrenadors ja està creada")

#         # Ens connectem a la basde de dades
#         def conexion():
#             try:
#                 conexion=sqlite3.connect("Futbol.bd")
#                 create_table(conexion)
#                 return conexion
#             except sqlite3.OperationalError:
#                 print("Error")

#         con = conexion()

#         def read():
#             cursor = con.cursor()
#             var_cursor = cursor.execute("SELECT score FROM Entrenadors").fetchone()
#             return var_cursor[0] + var_cursor[1]

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

        self.estadistica = Estadistica()
        #self.aboutFinestra = About()

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

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

        icon_path = os.path.join(ruta_base, "PNGs/smiley-medium.png")
        about = QAction(QIcon(icon_path), "&About", self)
        about.setStatusTip("About")
        about.triggered.connect(self.finestraAbout)

        menu = self.menuBar()

        menu_action = menu.addMenu("&Options")
        menu_action.addAction(LogOut)
        menu_action.addAction(about)
        menu_action.addAction(salir)
        
        # Layouts
        layoutUser = QVBoxLayout()
        layoutTopSide = QHBoxLayout()
        layoutEquips = QVBoxLayout()
        layoutJugadors = QVBoxLayout()
        layoutBoto = QVBoxLayout()

        # Layout Equips
        labelEquips = QLabel()
        labelEquips.setText("Mis Equipos")

        boxEquips = QComboBox()
        boxEquips.addItem("Prebenjamin A")
        boxEquips.addItem("Alevin B")
        
        layoutEquips.addWidget(labelEquips)
        layoutEquips.addWidget(boxEquips)
        

        # Layout Jugadors
        labelJugadors = QLabel()
        labelJugadors.setText("Jugadores")

        boxJuagdors = QComboBox()
        llistaJugadorsPrebenjamin = ["Antonio Garica", "Jose Martinez", "Francisco Lopez", 
        "Juan Sanchez", "Pedro Gomez", "Jesus Fernandez"
        ]
        llistaJugadorsAlevin = ["Andres Cano", "Ramon Garrido", "Enrique Gil", "Alvaro Ortiz", 
        "Emilio Valero", "Diego Rodenas"
        ]

        for i in llistaJugadorsPrebenjamin:
            boxJuagdors.addItem(i)

        layoutJugadors.addWidget(labelJugadors)
        layoutJugadors.addWidget(boxJuagdors)

        #Boto
        labelEstadistica = QLabel("Estadistica de jugadores")
        botoEstadistica = QPushButton("Estadistica")
        layoutBoto.addWidget(labelEstadistica)
        layoutBoto.addWidget(botoEstadistica)  
        botoEstadistica.clicked.connect(self.checkInEstadistica)  

        layoutUser.addWidget(centralWidget)
        layoutUser.addLayout(layoutTopSide)
        layoutTopSide.addLayout(layoutEquips)
        layoutTopSide.addLayout(layoutJugadors)
        layoutTopSide.addLayout(layoutBoto)


        widget = QWidget()
        widget.setLayout(layoutUser)
        self.setCentralWidget(widget)


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
    
    def checkInEstadistica(self):
        self.hide()
        self.estadistica.show()

    def finestraAbout(self):
        self.hide()
        #self.aboutFinestra.show()


# Pantalla de registrarse
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.estadistica = Estadistica()

        self.setWindowTitle("Register")

        # Llista on guardem el usuaris
        self.llista_usuaris = []

        # Llista on guardem les contrasenyes
        self.llista_passwd = []

        layout_register = QVBoxLayout()
        self.label_register = QLabel("", self)

        # Creem el LineEdit per a l'usuari
        self.usuari_register = QLineEdit()
        self.usuari_register.setPlaceholderText("Usuario")
        layout_register.addWidget(self.usuari_register)

        # Creem el LineEdit per a la contrasenya
        self.passwd_register = QLineEdit()
        self.passwd_register.setPlaceholderText("Contraseña")
        layout_register.addWidget(self.passwd_register)

        # PER A COMPROVAR QUE EL USUARI I LA CONTRASNEYA SON CORRECTES COMPROVAREM 
        # LA POSIUCIO DE LA LLISTA DEL ELEMENT EN 2 for PER A SABER SI SON 
        # LES INTRODUIDES PER EL MATEIX USUARI

        # Creem el botó de registrarse
        button = QPushButton("Registrarse")
        button.clicked.connect(self.registrarse)
        layout_register.addWidget(button)

        icon_path = os.path.join(ruta_base, "PNGs/navigation-180.png")
        action_register = QAction(QIcon(icon_path),"&Back to Login", self)
        action_register.setStatusTip("Login")
        action_register.triggered.connect(self.tornarLogin)

        menu = self.menuBar()

        menu_register = menu.addMenu("&Options")
        menu_register.addAction(action_register)

        layout_register.addWidget(self.label_register)

        widget = QWidget()
        widget.setLayout(layout_register)
        self.setCentralWidget(widget)

    def registrarse(self):
        if (len(self.llista_usuaris)) == 0 and (len(self.llista_passwd) == 0):
            self.llista_usuaris.append(self.usuari_register.text())
            self.llista_passwd.append(self.passwd_register.text())
        else:
            for i in self.llista_usuaris:
                if self.usuari_register.text() == i:
                    # Traure un dialog
                    print("Aquest nom ja esta en us")
        # LA COMPROVACIO AMB EL REGISTERL LA FAREM EN EL NOM SOLS
        # AQUESTA ES LA COMPROVACIO DEL LOGIN(provar amb el mètode zip)
        # else:
        #     for i in self.llista_usuaris:
        #         if (self.usuari_register.text() == i):
        #             index_i = self.llista_usuaris.index(i)
        #             for j in self.llista_passwd:
        #                 if (self.passwd_register.text() == j[index_i]):
        #                     print("Correcte")
        #                 else:
        #                     print("Usuari o contrasenya incorrectes")
        #         else:
        #             # Tindriem  que traure un dialeg digent-ho
        #             print("Aquest nom d'usuari ja esta en us")
    
    # Tornar a la pantalla de Login
    def tornarLogin(self):
        self.hide()
        if (__name__ == '__main__'):
            self = MainWindow()
            if (__name__ == '__main__'):
                w.show()


class Estadistica(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estadisticas")
        #self.user = User()

        layout = QVBoxLayout()

        # Jornades
        labelJornades = QLabel()
        labelJornades.setText("Jornadas")

        boxJornadas = QComboBox()
        listaJornadas = ["1", "2", "3", "4", "5"]
        # listaJornadas(range(1, 21))

        for i in listaJornadas:
            boxJornadas.addItem("Jornada " + i)

        layout.addWidget(labelJornades)
        layout.addWidget(boxJornadas)

        # Goles
        labelGoles = QLabel("Goles:")
        spinGoles = QSpinBox()
        spinGoles.setMaximum(15)
        spinGoles.setMinimum(0)

        layout.addWidget(labelGoles)
        layout.addWidget(spinGoles)
        
        # Minutos
        labelMinutos = QLabel("Minutos jugados:")
        spinMinutos = QSpinBox()
        spinMinutos.setMaximum(50)
        spinMinutos.setMinimum(0)

        layout.addWidget(labelMinutos)
        layout.addWidget(spinMinutos)

        # Actitud
        labelActitud = QLabel("Actitud:")
        actitud = QSpinBox()
        actitud.setMaximum(5)
        actitud.setMinimum(1)

        layout.addWidget(labelActitud)
        layout.addWidget(actitud)

        # Creem el botó de guardar
        buttonGuardar = QPushButton("Guardar")
        layout.addWidget(buttonGuardar)
        buttonGuardar.clicked.connect(self.guardar)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def guardar(self):
        self.hide()
        #self.user.show()

class About(QMainWindow):
    def __init__(self):
        super().__init__()

        self.user = User()

        self.setWindowTitle("About")
        layoutAbout = QVBoxLayout()

        labelAbout = QLabel("About")
        layoutAbout.addWidget(labelAbout)

        icon_path = os.path.join(ruta_base, "PNGs/navigation-180.png")
        actionAbout = QAction(QIcon(icon_path),"&Tornar al usuari", self)
        actionAbout.setStatusTip("Login")
        actionAbout.triggered.connect(self.tornarUser)

        menu = self.menuBar()

        menuAbout = menu.addMenu("&Opcions")
        menuAbout.addAction(actionAbout)

        widget = QWidget()
        widget.setLayout(layoutAbout)
        self.setCentralWidget(widget)
    
    def tornarUser(self):
        self.hide()
        self.user.show()
        
        

# Pantalla Login
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        self.user = User()
        self.admin = Admin()
        self.register = Register()

        layout = QVBoxLayout()

        self.label = QLabel("", self)

        # Creem el LineEdit per a l'usuari
        self.usuari = QLineEdit("user")
        self.usuari.setPlaceholderText("Usuario")
        layout.addWidget(self.usuari)

        # Creem el LineEdit per a la contrasenya
        self.passwd = QLineEdit("1234")
        self.passwd.setPlaceholderText("Contraseña")
        layout.addWidget(self.passwd)

        # Creem el botó de Login 
        button = QPushButton("Login")
        button.clicked.connect(self.checkIn)
        layout.addWidget(button)

        icon_path = os.path.join(ruta_base, "PNGs/cross-button.png")
        salir = QAction(QIcon(icon_path), "&Salir", self)
        salir.setStatusTip("Salir")
        salir.triggered.connect(self.exit)

        icon_path = os.path.join(ruta_base, "PNGs/safe--pencil.png")
        register = QAction(QIcon(icon_path),"&Register", self)
        register.setStatusTip("Registrarse")
        register.triggered.connect(self.pantalla_register)

        menu = self.menuBar()

        menu_principal = menu.addMenu("&Options")
        menu_principal.addAction(salir)
        menu_principal.addAction(register)

        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Funcio per a entrar en la pantalla indicada
    def checkIn(self):
        if self.usuari.text() == "admin" and self.passwd.text() == "1234":
            self.hide()
            self.admin.show()
        elif self.usuari.text() == "user" and self.passwd.text() == "1234":
            self.hide()
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

    def pantalla_register(self):
        self.hide()
        self.register.show()



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()