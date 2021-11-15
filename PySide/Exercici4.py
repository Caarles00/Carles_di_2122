from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        ample = 500
        llarg = 500

        self.setFixedSize(QSize(ample, llarg))
        self.setWindowTitle("Default")

        self.pybutton = QPushButton('Maximitza', self)
        self.pybutton1 = QPushButton('Normalitza', self)
        self.pybutton2 = QPushButton('Minimitza', self)
        
        #Connectem la senyal clicked a la ranura button_pressed
        self.pybutton.clicked.connect(self.max) 
        self.pybutton1.clicked.connect(self.normal)
        self.pybutton2.clicked.connect(self.min)

        self.pybutton.resize(100, 50)
        self.pybutton.move(50, ample//2)

        self.pybutton1.resize(100, 50)
        self.pybutton1.move(200, ample//2)

        self.pybutton2.resize(100, 50)
        self.pybutton2.move(350, ample//2)

    def max(self):
        ample = 800
        llarg = 800

        self.setFixedSize(QSize(ample, llarg))
        self.setWindowTitle("Maximitzat")
        #self.setWindowFlag(self.setDisabled);

        self.pybutton.move(200, ample//2)
        self.pybutton1.move(350, ample//2)
        self.pybutton2.move(500, ample//2)

    def min(self):
        ample = 300
        llarg = 300

        self.setFixedSize(QSize(ample, llarg))
        self.setWindowTitle("Minimitzat")

        self.pybutton.move(0, ample//2)
        self.pybutton1.move(100, ample//2)
        self.pybutton2.move(200, ample//2)

    def normal(self):
        ample = 500
        llarg = 500

        self.setFixedSize(QSize(ample, llarg))
        self.setWindowTitle("Normal")

        self.pybutton.move(50, ample//2)
        self.pybutton1.move(200, ample//2)
        self.pybutton2.move(350, ample//2)

if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()