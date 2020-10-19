import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cur_img = 'upii.jpg'
        self.initUI
        self.button_r.clicked.connect(self.run)


    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('PI2.dgzDzgG0')
        self.button_r = QPushButton(self)
        self.button_r.move(10, 20)
        self.button_r.resize(30, 50)
        self.button_r.setText('R')
        # self.button_g = QPushButton(self)
        # self.button_r = QPushButton(self)

        """
        блаблаблаблаблаблабалблаблаблаблабла
        """
        self.pixmap = QPixmap(self.cur_img)
        self.img = QLabel(self)
        self.img.setPixmap(self.pixmap)
        self.img.move(200, 30)
        self.img.resize(400, 400)

    def run(self):
        sander = self.sender().text()
        img


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
