import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")

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

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)
        self.setFixedSize(350,200)

    
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

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()