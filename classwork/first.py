import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
import csv


class MyTable(QMainWindow):
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTable()
    ex.show()
    sys.exit(app.exec_())