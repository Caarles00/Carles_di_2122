import sys
import os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QToolBar,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QStatusBar
)

ruta_base = os.path.dirname(__file__)


class CalcNormal(QGridLayout):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.layout_bottons = QGridLayout()
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        #self.addToolBar(toolbar)

        self.line = QLineEdit()
        self.line.setAlignment(Qt.AlignRight)
        self.line.setReadOnly(True)
        self.main_layout.addWidget(self.line)

        self.store = ""
        self.checkParentesi = True
        self.line.setText(self.store)

        self.main_layout.addLayout(self.layout_bottons)

        # Etiquetes dels botons
        self.etiquetes = {"√": (0, 0), "π": (0, 1), "^": (0, 2), "!": (0, 3), 
                     "AC": (1, 0), "()": (1, 1), "%": (1, 2), "/": (1, 3),
                     "7": (2, 0), "8": (2, 1), "9": (2, 2), "x": (2, 3),
                     "4": (3, 0), "5": (3, 1), "6": (3, 2), "+": (3, 3),
                     "1": (4, 0), "2": (4, 1), "3": (4, 2), "-": (4, 3),
                     "0": (5, 0), ".": (5, 1), "←": (5, 2), "=": (5, 3)}
        
        for posicio, etiqueta in self.etiquetes.items():
            self.etiquetes[posicio] = QPushButton(posicio)
            self.layout_bottons.addWidget(self.etiquetes[posicio], etiqueta[0], etiqueta[1])
            self.etiquetes[posicio].clicked.connect(self.operacions)
        
        self.main_layout.addLayout(self.layout_bottons)
        self.setStatusBar(QStatusBar(self))

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

class CalcCientifica(QGridLayout):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Científica")

        self.main_layout = QVBoxLayout()
        self.layout_bottons = QGridLayout()

        self.line = QLineEdit()
        self.line.setAlignment(Qt.AlignRight)
        self.line.setReadOnly(True)
        self.main_layout.addWidget(self.line)
        
        self.store = ""
        self.checkParentesi = True
        self.line.setText(self.store)

        self.main_layout.addLayout(self.layout_bottons)

        # Etiquetes dels botons
        self.etiquetes = {"√": (0, 0), "π": (0, 1), "^": (0, 2), "!": (0, 3), "sin": (0, 4), "cos": (0, 5), "tan": (0, 6),
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
        
        self.main_layout.addLayout(self.layout_bottons)
        self.setStatusBar(QStatusBar(self))

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.store_operacions = ""

        layout = QStackedLayout()
        
        #Afegim els widgets sobre altres
        layout.addWidget(CalcNormal)
        layout.addWidget(CalcCientifica)

        icon_path = os.path.join(ruta_base, "calculator--plus.png")
        self.button_action = QAction(QIcon(icon_path), "Científica", self)
        self.button_action.toggled.connect(self.onMyToolBarButtonClick)
        self.button_action.setCheckable(True)

        icon_path = os.path.join(ruta_base, "cross-button.png")
        self.button2_action = QAction(QIcon(icon_path), "Eixir", self)
        self.button2_action.toggled.connect(self.onMyToolBarButtonClick)
        self.button2_action.setCheckable(True)

        icon_path = os.path.join(ruta_base, "safe--arrow.png")
        self.button3_action = QAction(QIcon(icon_path), "Guardar", self)
        self.button3_action.toggled.connect(self.onMyToolBarButtonClick)
        self.button3_action.setCheckable(True)

        icon_path = os.path.join(ruta_base, "calculator.png")
        self.button4_action = QAction(QIcon(icon_path), "Normal", self)
        self.button4_action.toggled.connect(self.onMyToolBarButtonClick)
        self.button4_action.setCheckable(True)

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.button2_action)
        file_menu.addAction(self.button3_action)

        mode_menu = menu.addMenu("&Mode")
        mode_menu.addAction(self.button_action)
        mode_menu.addAction(self.button4_action)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.layout = layout

    
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
        self.line.setText(text)
        self.line.setFocus()

    def mostrarText(self, text):
        return self.line.text()
    
    def clear(self):
        self.posarText("")
        self.store = ""
    
    def onMyToolBarButtonClick(self, s):
        print("click", s)
    
    def menuPressEvent(self):
        index = self.layout.currentIdex()

        #Busquem l'index max del layout contant quants widgets tenim
        index_max = self.layout.count() - 1

        if (self.button4_action):
            # Si apretem en el mode cientific sumem 1 al index per a que el pose damunt i el mostre
            index += 1
            self.button_action.setCheckable(False)

        elif (self.button_action):
            # Si apretem en el mode normal restem 1 al index per a que el pose damunt i el mostre
            index -= 1
            self.button_action4.setCheckable(False)

        # Eixim de la calculadora
        elif (self.button2_action):
            self.quit()

        # Guardem les operacions
        elif (self.button3_action):
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
        
        # Generem efecte infinit
        if index > index_max:
            index = 0
        if index < 0:
            index = index_max
        
        # Establim el nou event
        self.layout.setCurrentIndex(index)
 
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()