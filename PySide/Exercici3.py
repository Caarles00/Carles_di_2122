from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
# Library to pass command arguments
import argparse


class MainWindow(QMainWindow):
    def __init__(self, args):
        super().__init__()
        title, text, fixed, size_x, size_y = "My Application", "Accept", False, 300, 200
        # Main window config
        if args.title:
            title = args.title
        if args.button_text:
            text = args.button_text
        if args.fixed_size:
            fixed = args.fixed_size
        if args.size:
            size_x, size_y = args.size
        self.setWindowTitle(title)
        self.setGeometry(600, 400, size_x, size_y)
        if(fixed):
            self.setFixedSize(size_x, size_y)

        # QPushButton
        self.button = QPushButton(text)
        self.setCentralWidget(self.button)
        self.button.clicked.connect(QApplication.instance().quit)
        self.statusBar().showMessage('Alfre')


def main():
    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--title", help="Title of application")
    parser.add_argument("-b", "--button-text", help="Button text")
    parser.add_argument("-f", "--fixed-size", action="store_true",
                        help="Window fixed size")
    parser.add_argument("-s", "--size", nargs=2, metavar=("SIZE_X", "SIZE_Y"), type=int,
                        help="Window's size")
    args = parser.parse_args()

    # PySide6
    app = QApplication(args)
    window = MainWindow(args)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()