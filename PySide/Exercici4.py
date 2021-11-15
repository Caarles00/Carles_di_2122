from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt
from config import AMPLE, LLARG, RESIZE_W, RESIZE_H

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(AMPLE, LLARG))
        self.setWindowTitle("Default")

        self.pybutton = QPushButton('Maximitza', self)
        self.pybutton1 = QPushButton('Normalitza', self)
        self.pybutton2 = QPushButton('Minimitza', self)
        
        #Connectem la senyal clicked a la ranura button_pressed
        self.pybutton.clicked.connect(self.max) 
        self.pybutton1.clicked.connect(self.normal)
        self.pybutton2.clicked.connect(self.min)

        self.pybutton.resize(RESIZE_W, RESIZE_H)
        self.pybutton.move(50, AMPLE//2)

        self.pybutton1.resize(RESIZE_W, RESIZE_H)
        self.pybutton1.move(200, AMPLE//2)

        self.pybutton2.resize(RESIZE_W, RESIZE_H)
        self.pybutton2.move(350, AMPLE//2)

    def max(self):
        ample = AMPLE + 300
        llarg = LLARG + 300

        self.setFixedSize(QSize(ample, llarg))
        self.setWindowTitle("Maximitzat")

        self.pybutton.move(200, ample//2)
        self.pybutton1.move(350, ample//2)
        self.pybutton2.move(500, ample//2)

        self.pybutton.setDisabled(True)
        self.pybutton1.setDisabled(False)
        self.pybutton2.setDisabled(False)

    def min(self):
        ample = AMPLE - 200
        llarg = LLARG - 200

        self.setFixedSize(QSize(ample, llarg))
        self.setWindowTitle("Minimitzat")

        self.pybutton.move(0, ample//2)
        self.pybutton1.move(100, ample//2)
        self.pybutton2.move(200, ample//2)

        self.pybutton.setDisabled(False)
        self.pybutton1.setDisabled(False)
        self.pybutton2.setDisabled(True)

    def normal(self):

        self.setFixedSize(QSize(AMPLE, LLARG))
        self.setWindowTitle("Normal")

        self.pybutton.move(50, AMPLE//2)
        self.pybutton1.move(200, AMPLE//2)
        self.pybutton2.move(350, AMPLE//2)

        self.pybutton.setDisabled(False)
        self.pybutton1.setDisabled(True)
        self.pybutton2.setDisabled(False)

if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()
