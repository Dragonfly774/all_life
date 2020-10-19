import sys

from PyQt5.QtWidgets import QWidget, QApplication

SLOVAR = {
    'Рубль': 1,
    'Доллар': 70,
    'Евро': 80,
    'Тубрик': 30
}

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('окно')
        self.setGeometry(300, 300, 300, 300)

        self.input_

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())