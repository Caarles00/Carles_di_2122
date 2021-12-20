import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                               QGridLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QStackedLayout, QStatusBar,
                               QVBoxLayout, QWidget)

ruta_base = os.path.dirname(__file__)

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Dialegs
        self.setWindowTitle("Dialeg eixir")

        self.buttons_dialog = QDialogButtonBox.Yes | QDialogButtonBox.No
        
        self.buttons_dialog = QDialogButtonBox(self.buttons_dialog)
        self.buttons_dialog.accepted.connect(self.accept)
        self.buttons_dialog.rejected.connect(self.reject)

        self.layout_dialeg = QVBoxLayout()
        mensatge = QLabel("Estas segur de que vols eixir?")
        self.layout_dialeg.addWidget(mensatge)
        self.layout_dialeg.addWidget(self.buttons_dialog)
        self.setLayout(self.layout_dialeg)   


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.store_operacions = ""

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # Creem el stackedLayout per a guardar el layout dels mode de la calculadora
        self.stackedLayout = QStackedLayout(self.widget)

        # Creem widget i layout per al mode normal
        self.CalcNormal = QWidget()
        self.layout_normal = QVBoxLayout(self.CalcNormal)
        self.CalcNormal.setLayout(self.layout_normal)

        # Creem widget i layout per al mode cientific
        self.CalcCientifia = QWidget()
        self.layout_cientifica = QVBoxLayout(self.CalcCientifia)
        self.CalcCientifia.setLayout(self.layout_cientifica)

        # Afegim els widgets al stackedLayout
        self.stackedLayout.addWidget(self.CalcNormal)
        self.stackedLayout.addWidget(self.CalcCientifia)

        # Botons del menu
        # Accio de la calculadora cientifica
        icon_path = os.path.join(ruta_base, "calculator--plus.png")
        self.button_action = QAction(QIcon(icon_path), "Científica", self)
        self.button_action.setStatusTip("Calculadora Científica")
        self.button_action.triggered.connect(self.cambiar_a_cientifica)

        # Accio de eixir
        icon_path = os.path.join(ruta_base, "cross-button.png")
        self.button2_action = QAction(QIcon(icon_path), "Eixir", self)
        self.button2_action.triggered.connect(self.eixir)

        # Accio de guardar
        icon_path = os.path.join(ruta_base, "safe--arrow.png")
        self.button3_action = QAction(QIcon(icon_path), "Guardar", self)
        self.button3_action.setStatusTip("Autoguardar")
        self.button3_action.triggered.connect(self.guardar)
        

        # Accio de la calculadora normal
        icon_path = os.path.join(ruta_base, "calculator.png")
        self.button4_action = QAction(QIcon(icon_path), "Normal", self)
        self.button4_action.setCheckable(True)
        self.button4_action.setStatusTip("Calculadora Normal")
        self.button4_action.triggered.connect(self.cambiar_a_normal)

        # Creem el menu
        menu = self.menuBar()

        # Afegim els submenus
        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.button2_action)
        file_menu.addAction(self.button3_action)

        mode_menu = menu.addMenu("&Mode")
        mode_menu.addAction(self.button_action)
        mode_menu.addAction(self.button4_action)

        # StatusBar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Calculadora Normal")
        self.statusLabel = QLabel('Guardar desactivat')
        self.statusBar.addPermanentWidget(self.statusLabel)

        if not self.button3_action.isChecked:
            self.statusLabel.setText("Guardar desactivat")
        else:
            self.statusLabel.setText("Guardar activat")
        

        # CALCULADORA NORMAL
        self.layout_bottons = QGridLayout()

        self.line = QLineEdit()
        self.line.setAlignment(Qt.AlignRight)
        self.line.setReadOnly(True)
        self.layout_normal.addWidget(self.line)

        self.store = ""
        self.checkParentesi = True
        self.line.setText(self.store)

        self.layout_normal.addLayout(self.layout_bottons)

        # Etiquetes dels botons
        self.etiquetes = {
            "√": (0, 0), "π": (0, 1), "^": (0, 2), "!": (0, 3), 
            "AC": (1, 0), "()": (1, 1), "%": (1, 2), "/": (1, 3),
            "7": (2, 0), "8": (2, 1), "9": (2, 2), "x": (2, 3),
            "4": (3, 0), "5": (3, 1), "6": (3, 2), "+": (3, 3),
            "1": (4, 0), "2": (4, 1), "3": (4, 2), "-": (4, 3),
            "0": (5, 0), ".": (5, 1), "←": (5, 2), "=": (5, 3)
            }
        
        
        for posicio, etiqueta in self.etiquetes.items():
            self.etiquetes[posicio] = QPushButton(posicio)
            self.layout_bottons.addWidget(self.etiquetes[posicio], etiqueta[0], etiqueta[1])
            self.etiquetes[posicio].clicked.connect(self.operacions)
        
        self.layout_normal.addLayout(self.layout_bottons)
        self.setStatusBar(QStatusBar(self))


        # CALCULADORA CIENTIFICA
        self.layout_bottons = QGridLayout()

        self.line_cient = QLineEdit()
        self.line_cient.setAlignment(Qt.AlignRight)
        self.line_cient.setReadOnly(True)
        self.layout_cientifica.addWidget(self.line_cient)
        
        self.store = ""
        self.checkParentesi = True
        self.line_cient.setText(self.store)

        self.layout_cientifica.addLayout(self.layout_bottons)

        # Etiquetes dels botons
        self.etiquetes = {
            "√": (0, 0), "π": (0, 1), "^": (0, 2), "!": (0, 3), "sin": (0, 4), "cos": (0, 5), "tan": (0, 6),
            "AC": (1, 0), "()": (1, 1), "%": (1, 2), "/": (1, 3), "sinh": (1, 4), "cosh": (1, 5), "tanh": (1, 6),
            "7": (2, 0), "8": (2, 1), "9": (2, 2), "x": (2, 3), "log": (2, 4), "ln": (2, 5), "e": (2, 6),
            "4": (3, 0), "5": (3, 1), "6": (3, 2), "+": (3, 3), "f(x)": (3, 4), "|x|": (3, 5), "1/x": (3, 6),
            "1": (4, 0), "2": (4, 1), "3": (4, 2), "-": (4, 3), "AxB": (4, 4), "Re": (4, 5), "lm": (4, 6),
            "0": (5, 0), ".": (5, 1), "←": (5, 2), "=": (5, 3), "conj": (5, 4), "Arg": (5, 5), "i": (5, 6)
                    }
        
        for posicio, etiqueta in self.etiquetes.items():
            self.etiquetes[posicio] = QPushButton(posicio)
            self.layout_bottons.addWidget(self.etiquetes[posicio], etiqueta[0], etiqueta[1])
            self.etiquetes[posicio].clicked.connect(self.operacions)
        
        self.layout_cientifica.addLayout(self.layout_bottons)
        self.setStatusBar(QStatusBar(self))


    def operacions(self):
        if (self.sender().text() == "="):
            self.posarText(str(eval(self.store)))
        elif (self.sender().text() == "←"):
            self.posarText(self.store[:-1])# Borra l'ultim digit de la calculadora
            self.store = self.store[:-1]
        elif (self.sender().text() == "x"):
            self.store += "*"
        elif (self.sender().text() == "AC"):
            self.clear()
        elif (self.sender().text() == "()"):
            if (self.checkParentesi):
                self.store += "("
                self.checkParentesi = False
            elif (not self.checkParentesi):
                self.store += ")"
                self.checkParentesi = False
        else:
            self.store += self.sender().text()
            self.posarText(self.store)


    def posarText(self, text):
        # Normal
        self.line.setText(text)
        self.line.setFocus()

        # Científica
        self.line_cient.setText(text)
        self.line_cient.setFocus()

    def mostrarText(self, text):
        return self.line.text()
    
    # Borrar
    def clear(self):
        self.posarText("")
        self.store = ""

    # Funció per a cambiar a la Calculadora Normal 
    def cambiar_a_normal(self):
        if self.button_action.isChecked:
            self.button_action.setCheckable(False)
            self.button4_action.setCheckable(True)

        self.stackedLayout.setCurrentWidget(self.CalcNormal)

        self.posarText("")
        self.store = ""

        self.statusBar.showMessage("Calculadora Normal")

    # Funció per a cambiar a la Calculadora Cientifica  
    def cambiar_a_cientifica(self):
        if self.button4_action.isChecked:
            self.button4_action.setCheckable(False)
            self.button_action.setCheckable(True)

        self.stackedLayout.setCurrentWidget(self.CalcCientifia)

        if self.button4_action.isChecked:
            self.button4_action.setCheckable(False)
            self.button_action.setCheckable(True)
        else:
            self.button_action.setCheckable(True)

        self.posarText("")
        self.store = ""

        self.statusBar.showMessage("Calculadora Cientifica")

    # Guardar en el .txt    
    def guardar(self):
        self.button3_action.setCheckable(True)
        try:
            resultats = os.path.join(os.path.dirname(__file__), "resultats.txt")
            with open(resultats, "a+") as f:
                f.write(self.store_operacions)
                f.write("\n")
                f.close()
        except FileNotFoundError as fnfe:
            return fnfe
        except IOError as ioe:
            return ioe

    # Eixir
    def eixir(self):
        dlg = CustomDialog()
        if dlg.exec_():
            exit()
        else:
            pass

 
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

