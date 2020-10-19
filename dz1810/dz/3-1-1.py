import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

alfa = {'a': '.-', 'b': '-...',
         'c': '-.-.', 'd': '-..', 'e': '.',
         'f': '..-.', 'g': '--.', 'h': '....',
         'i': '..', 'j': '.---', 'k': '-.-',
         'l': '.-..', 'm': '--', 'n': '-.',
         'o': '---', 'p': '.--.', 'q': '--.-',
         'r': '.-.', 's': '...', 't': '-',
         'u': '..-', 'v': '...-', 'w': '.--',
         'x': '-..-', 'y': '-.--', 'z': '--..'}


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 350, 500, 200)
        for i in range(26):
            if i > 13:
                n = list(alfa.keys())[i]
                self.button = QPushButton(n, self)
                self.button.resize(25, 25)
                self.button.move(15 + (i - 13) * 30, 40)
                self.button.clicked.connect(self.run)
            else:
                n = list(alfa.keys())[i]
                self.button = QPushButton(n, self)
                self.button.resize(25, 25)
                self.button.move(15 + i * 30, 10)
                self.button.clicked.connect(self.run)
            self.lineEdit = QLineEdit(self)
            self.lineEdit.resize(420, 40)
            self.lineEdit.move(10, 70)

    def run(self):
        self.lineEdit.setText(self.lineEdit.text() + ' ' + alfa[self.sender().text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
